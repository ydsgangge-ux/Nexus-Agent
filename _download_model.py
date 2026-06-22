"""从国内镜像下载 sentence-transformers 模型
使用方法：
  本机：   python _download_model.py
  云服务器： python _download_model.py

如果网络访问 huggingface.co 有问题，本脚本会自动使用 hf-mirror.com 镜像。
首次下载约 470MB，需要几分钟。
"""
import os
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

from sentence_transformers import SentenceTransformer

print("[下载] 正在从 hf-mirror.com 下载向量模型...")
print("[下载] 模型: paraphrase-multilingual-MiniLM-L12-v2")
print("[下载] 大小: ~470MB，首次下载需要几分钟...")
print()

m = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

print()
print(f"[OK] 下载完成！")
print(f"[OK] 向量维度: {m.get_sentence_embedding_dimension()}")
print(f"[OK] 设备: {m.device}")

# 验证一下，用中文测试
vec = m.encode("你好世界", normalize_embeddings=True)
print(f"[OK] 编码测试通过，向量前5维: {vec[:5].tolist()}")