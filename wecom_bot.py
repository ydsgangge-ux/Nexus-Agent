"""
wecom_bot.py
企业微信智能机器人 — 长连接客户端
基于 wecom-aibot-sdk-python，自动处理认证、心跳、断线重连

使用方式：
    1. pip install wecom-aibot-sdk-python
    2. 配置 bot_id/secret（环境变量或 ha_config.json）
    3. server_start.py 中启动
"""
import json
import logging
import os
from pathlib import Path

from wecom_aibot_sdk import WSClient, generate_req_id


def _load_wecom_config() -> dict:
    """读取企业微信配置（环境变量 > ha_config.json）"""
    # 环境变量优先
    bot_id = os.environ.get("WECOM_BOT_ID", "")
    secret = os.environ.get("WECOM_BOT_SECRET", "")
    if bot_id and secret:
        return {"bot_id": bot_id, "secret": secret}

    # ha_config.json 兜底
    try:
        cfg_path = Path(__file__).parent / "ha_config.json"
        if cfg_path.exists():
            cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
            bot_id = cfg.get("wecom_bot_id", "") or cfg.get("bot_id", "")
            secret = cfg.get("wecom_bot_secret", "") or cfg.get("bot_secret", "")
            if bot_id and secret:
                return {"bot_id": bot_id, "secret": secret}
    except Exception:
        pass

    return {}


class WecomBot:
    """
    企业微信智能机器人
    将企业微信消息桥接到 agent.process()
    """

    def __init__(self, agent, bot_id: str = "", secret: str = ""):
        self._agent = agent
        config = _load_wecom_config()
        self._bot_id = bot_id or config.get("bot_id", "")
        self._secret = secret or config.get("secret", "")
        self._client = None

    async def start(self):
        """启动企业微信长连接"""
        if not self._bot_id or not self._secret:
            print("[WecomBot] 未配置 bot_id/secret，跳过启动")
            print("[WecomBot] 在 ha_config.json 中添加: wecom_bot_id / wecom_bot_secret")
            return

        # 日志配置
        logger = logging.getLogger("wecom_aibot")
        logger.setLevel(logging.WARNING)

        self._client = WSClient(
            {
                "bot_id": self._bot_id,
                "secret": self._secret,
                "logger": logger,
            }
        )

        # ── 注册事件回调 ──

        async def on_text(frame):
            """收到文本消息 → 先发占位 → 调用 A 层 → 替换为最终回复"""
            body = frame.body
            content = body.get("text", {}).get("content", "")
            chatid = body.get("chatid", "")
            msgid = body.get("msgid", "")

            if not content.strip():
                return

            from_user = body.get("from", {})
            wecom_uid = from_user.get("userid", "") if isinstance(from_user, dict) else ""
            print(f"[WecomBot] 收到消息: {content[:80]}")
            print(f"[WecomBot]  来自={wecom_uid}  chatid={chatid}  msgid={msgid}")

            # 第一步：立刻发占位消息（企业微信要求5秒内必须回复）
            import asyncio as _asyncio
            stream_id = generate_req_id("stream")
            try:
                await self._client.reply_stream(
                    frame, stream_id, "焕灵正在思考…", finish=False
                )
            except Exception:
                pass  # 占位消息失败不阻塞主流程

            # 第二步：调用 A 层（可能耗时较久，但5秒限制已用占位消息绕过）
            try:
                wecom_uname = f"企微_{wecom_uid}" if wecom_uid else ""
                result = await _asyncio.to_thread(
                    self._agent.process, content,
                    override_uid=f"wecom_{wecom_uid}" if wecom_uid else "",
                    override_uname=wecom_uname,
                )
                reply = (
                    result.get("response")
                    or result.get("reply")
                    or result.get("text")
                    or "好的，我知道了。"
                )
            except Exception as e:
                print(f"[WecomBot] A层处理异常: {e}")
                reply = f"抱歉，我遇到了一点问题：{e}"

            # 第三步：发最终结果（用 send_message 主动推送，不依赖原会话）
            try:
                await self._client.send_message(chatid, {
                    "msgtype": "text",
                    "text": {"content": reply},
                })
                print(f"[WecomBot] 已回复: {reply[:80]}")
            except Exception as e:
                print(f"[WecomBot] 回复失败: {e}")
                # 最终兜底：尝试 reply_stream
                try:
                    await self._client.reply_stream(frame, stream_id, reply, finish=True)
                except Exception:
                    pass

        async def on_enter(frame):
            """用户进入会话 → 发送欢迎语"""
            print("[WecomBot] 用户进入会话")
            try:
                await self._client.reply_welcome(frame, {
                    "msgtype": "text",
                    "text": {"content": "你好！我是焕灵，有什么可以帮你的？"},
                })
            except Exception as e:
                print(f"[WecomBot] 欢迎消息发送失败: {e}")

        async def on_connected(*args):
            print("[WecomBot] 长连接已建立 ✅")

        async def on_auth(*args):
            print("[WecomBot] 认证成功 ✅")

        async def on_disconnected(reason):
            print(f"[WecomBot] 连接断开: {reason}")

        async def on_reconnecting(attempt, *args):
            print(f"[WecomBot] 正在重连（第{attempt}次）...")

        # 用回调方式注册
        self._client.on("message.text", on_text)
        self._client.on("event.enter_chat", on_enter)
        self._client.on("connected", on_connected)
        self._client.on("authenticated", on_auth)
        self._client.on("disconnected", on_disconnected)
        self._client.on("reconnecting", on_reconnecting)

        # ── 建立连接（带自动重连）──
        import asyncio as _asyncio
        while True:
            try:
                await self._client.connect_async()
                # 保持运行直到断开
                while self._client.is_connected:
                    await _asyncio.sleep(1)
            except Exception as e:
                print(f"[WecomBot] 连接异常: {e}")
            print(f"[WecomBot] 连接断开，5秒后重连...")
            await _asyncio.sleep(5)
