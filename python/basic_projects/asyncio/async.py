import asyncio

async def fetch_data() -> dict:
    print("start_fetching")
    await asyncio.sleep(2)
    print("done fetching")
    await asyncio.sleep(2)
    return {'data': 1}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def main():
    task1 = asyncio.create_task(fetch_data())
    value = await task1
    task2 = asyncio.create_task(print_numbers())

    await task2

asyncio.run(main())