from dotenv import load_dotenv
from agents import (
    # AsyncOpenAI,
    set_default_openai_client,
    set_tracing_disabled,
    OpenAIChatCompletionsModel,
    ModelSettings,
)
import os
import asyncio
from langfuse.openai import AsyncOpenAI

load_dotenv()


external_client = AsyncOpenAI(
    base_url="https://api.siliconflow.cn/v1",
    api_key=os.getenv("SILICONFLOW_API_KEY"),
)

set_default_openai_client(external_client)
set_tracing_disabled(True)

ds_model = OpenAIChatCompletionsModel(
    model="Pro/deepseek-ai/DeepSeek-R1", openai_client=external_client
)
