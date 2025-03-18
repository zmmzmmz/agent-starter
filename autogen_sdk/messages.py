from io import BytesIO

import requests
from autogen_agentchat.messages import MultiModalMessage, TextMessage
from autogen_core import Image as AGImage
from PIL import Image

# 文本消息
TextMessage(content="你好啊，你是谁", source="User")

# 多模态消息
pil_image = Image.open(BytesIO(requests.get("https://picsum.photos/300/200").content))
img = AGImage(pil_image)
multi_modal_message = MultiModalMessage(
    content=["Can you describe the content of this image?", img], source="User"
)
img
