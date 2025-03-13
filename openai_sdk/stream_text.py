import asyncio

from agent import ds_model

from openai.types.responses import ResponseTextDeltaEvent

from agents import Agent, Runner


async def main():
    agent = Agent(
        name="Joker",
        model=ds_model,
        instructions="You are a helpful assistant.",
    )

    result = Runner.run_streamed(agent, input="告诉我3个冷笑话")
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(
            event.data, ResponseTextDeltaEvent
        ):
            print(event.data.delta, end="", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
