from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    set_tracing_disabled,
    set_default_openai_client,
    ModelSettings,
)


from dotenv import load_dotenv
import os
import asyncio

load_dotenv()


async def main():

    external_client = AsyncOpenAI(
        base_url="https://api.siliconflow.cn/v1",
        api_key=os.getenv("SILICONFLOW_API_KEY"),
    )

    set_default_openai_client(external_client)
    set_tracing_disabled(True)

    ds_model = OpenAIChatCompletionsModel(
        model="Pro/deepseek-ai/DeepSeek-R1", openai_client=external_client
    )
    agent = Agent(
        name="Assistant",
        instructions="你是个满嘴骚话的酒鬼，无论别人怎么给你说，你只会给他讲酒后真言",
        model=ds_model,
        model_settings=ModelSettings(temperature=0.9),
    )

    result = await Runner.run(agent, "你是谁？为什么出现在我床上")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
