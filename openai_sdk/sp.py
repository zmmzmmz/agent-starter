from agents import Agent, Runner, ModelSettings, function_tool
from agent import ds_model


from dotenv import load_dotenv
import asyncio

load_dotenv()


@function_tool
def get_task_status_count():
    """Get task status Count by Suppier Name"""
    return 2


async def main():

    agent = Agent(
        name="Assistant",
        instructions="你是个有用的助手",
        model=ds_model,
        tools=[get_task_status_count],
        model_settings=ModelSettings(temperature=0.1, top_p=0.95),
    )

    result = await Runner.run(agent, "帮我查询供应商王哥待推款商品还有哪些")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
