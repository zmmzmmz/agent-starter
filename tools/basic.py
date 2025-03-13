from dotenv import load_dotenv
import os
from langfuse.openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://api.siliconflow.cn/v1", api_key=os.getenv("SILICONFLOW_API_KEY")
)


def get_weather():
    return "今天天气很好啊"


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a given city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "The name of the city to query weather for.",
                    },
                },
                "required": ["city"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_task_status_count",
            "description": "Get task status Count by Suppier Name",
            "parameters": {
                "type": "object",
                "properties": {
                    "status": {
                        "type": "string",
                        "description": "The name of the task to query.",
                    },
                    "supplier": {
                        "type": "string",
                        "description": "The name of supplier.",
                    },
                },
                "required": ["status"],
            },
        },
    },
]


def function_call_playground(prompt):
    messages = [{"role": "user", "content": prompt}]

    responses = client.chat.completions.create(
        model="Pro/deepseek-ai/DeepSeek-V3",
        messages=messages,
        tools=tools,
        temperature=0.01,
        top_p=0.95,
        stream=False,
    )

    print(responses)


function_call_playground("帮我查询供应商王哥待推款商品还有哪些?")
