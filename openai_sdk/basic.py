from agents import (
    Agent,
    Runner,
    ModelSettings,
)
from agent import ds_model


from dotenv import load_dotenv
import asyncio

load_dotenv()


async def main():

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
