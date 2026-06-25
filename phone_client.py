"""
phone_client.py
手机 WebSocket 客户端
============================
在 Termux 里运行，连接云端，响应截图指令。

安装：
    pkg install python
    pip install websockets requests

运行：
    python phone_client.py

配置：修改下方 CLOUD_WS_URL 和 WS_TOKEN
"""
import asyncio
import json
import base64
import requests
import time
import sys
from datetime import datetime

# ── 配置（修改这里）──────────────────────────────────────────
CLOUD_WS_URL = "ws://123.56.65.97:18766"    # 云端 WebSocket 地址
WS_TOKEN = "agi2025202620272028"             # 认证 token（与云端一致）
IP_WEBCAM_URL = "http://localhost:8080"      # IP Webcam 本地地址
RECONNECT_INTERVAL = 5                       # 断线重连间隔（秒）
HEARTBEAT_INTERVAL = 30                      # 心跳间隔（秒）


def capture_frame() -> bytes:
    """从 IP Webcam 拿当前截图"""
    try:
        resp = requests.get(
            f"{IP_WEBCAM_URL}/shot.jpg",
            timeout=5
        )
        if resp.status_code == 200 and len(resp.content) > 1000:
            return resp.content
    except Exception as e:
        print(f"[Client] 截图失败: {e}")
    return b""


def get_sensors() -> dict:
    """从 IP Webcam 获取传感器数据"""
    try:
        resp = requests.get(
            f"{IP_WEBCAM_URL}/sensors.json",
            timeout=5
        )
        if resp.status_code == 200:
            return resp.json()
    except Exception as e:
        print(f"[Client] 传感器读取失败: {e}")
    return {}


def format_sensor_data(raw: dict) -> dict:
    """将 IP Webcam 原始传感器数据格式化为统一格式"""
    gps = raw.get("gps", {})
    battery = raw.get("battery_level", {}).get("data", [0])[0]
    light = raw.get("light", {}).get("data", [0])[0]
    accel = raw.get("accelerometer", {}).get("data", [0, 0, 0])

    return {
        "gps": {
            "lat": gps.get("lat", 0.0),
            "lng": gps.get("lng", 0.0),
            "accuracy": gps.get("accuracy", 0.0)
        },
        "battery": battery,
        "light": light,
        "accelerometer": accel,
        "timestamp": datetime.now().isoformat()
    }


async def handle_server(websocket):
    """处理云端发来的消息"""
    print("[Client] 已连接云端，等待指令...")

    # 认证
    await websocket.send(json.dumps({
        "type": "token",
        "token": WS_TOKEN,
    }))

    # 等待认证结果
    try:
        raw = await asyncio.wait_for(websocket.recv(), timeout=10)
        auth_resp = json.loads(raw)
        if auth_resp.get("type") != "auth_ok":
            print(f"[Client] 认证失败: {auth_resp}")
            return
        print("[Client] 认证成功")
    except asyncio.TimeoutError:
        print("[Client] 认证超时")
        return

    # 心跳任务
    async def heartbeat():
        while True:
            try:
                await websocket.send(json.dumps({"type": "ping"}))
                await asyncio.sleep(HEARTBEAT_INTERVAL)
            except Exception:
                break

    asyncio.create_task(heartbeat())

    async for message in websocket:
        try:
            data = json.loads(message)
            msg_type = data.get("type")

            if msg_type == "capture_request":
                request_id = data.get("request_id", "")
                print(f"[Client] 收到截图指令: {request_id}")

                img_bytes = capture_frame()

                if img_bytes:
                    # 二进制帧传输：request_id(8字节补齐) + JPEG
                    rid_bytes = request_id.encode("ascii")[:8].ljust(8)
                    await websocket.send(rid_bytes + img_bytes)
                    print(f"[Client] 截图已返回: {len(img_bytes)} bytes")
                else:
                    # 截图失败，返回空响应
                    await websocket.send(json.dumps({
                        "type": "frame_response",
                        "request_id": request_id,
                        "image": "",
                    }))

            elif msg_type == "sensor_request":
                request_id = data.get("request_id", "")
                print(f"[Client] 收到传感器请求: {request_id}")

                raw = get_sensors()
                sensor_data = format_sensor_data(raw) if raw else {}

                await websocket.send(json.dumps({
                    "type": "sensor_response",
                    "request_id": request_id,
                    "data": sensor_data
                }))
                print(f"[Client] 传感器数据已返回")

            elif msg_type == "pong":
                pass

        except Exception as e:
            print(f"[Client] 处理消息错误: {e}")


async def main():
    """主循环，自动重连"""
    print(f"[Client] 目标: {CLOUD_WS_URL}")
    print(f"[Client] IP Webcam: {IP_WEBCAM_URL}")
    print()

    while True:
        try:
            async with websockets.connect(CLOUD_WS_URL) as websocket:
                await handle_server(websocket)
        except Exception as e:
            print(f"[Client] 连接失败: {e}")
        print(f"[Client] {RECONNECT_INTERVAL}秒后重连...")
        await asyncio.sleep(RECONNECT_INTERVAL)


if __name__ == "__main__":
    # 检查依赖
    try:
        import websockets
    except ImportError:
        print("缺少依赖: pip install websockets")
        sys.exit(1)
    try:
        import requests
    except ImportError:
        print("缺少依赖: pip install requests")
        sys.exit(1)

    asyncio.run(main())
