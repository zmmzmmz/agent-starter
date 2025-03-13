import random
from agent import ds_model
import asyncio
from agents import Agent, function_tool, Runner, ItemHelpers


@function_tool
def how_many_jokes() -> int:
    return random.randint(1, 10)


async def main():
    agent = Agent(
        name="Joker",
        instructions="开始就调用 `how_many_jokes`, 然后给我讲多个故事",
        model=ds_model,
        tools=[how_many_jokes],
    )

    result = await Runner.run(
        agent,
        input="Hello",
    )

    print("res", result)
    print("=== 开始动了 ===")
    async for event in result.stream_events():
        # We'll ignore the raw responses event deltas
        if event.type == "raw_response_event":
            continue
        elif event.type == "agent_updated_stream_event":
            print(f"Agent 更新: {event.new_agent.name}")
            continue
        elif event.type == "run_item_stream_event":
            if event.item.type == "tool_call_item":
                print("-- 工具被调用")
            elif event.item.type == "tool_call_output_item":
                print(f"-- 工具执行结果: {event.item.output}")
            elif event.item.type == "message_output_item":
                print(f"-- 消息结果:\n {ItemHelpers.text_message_output(event.item)}")
            else:
                pass  # Ignore other event types

    print("=== 结束了 ===")


if __name__ == "__main__":
    asyncio.run(main())
