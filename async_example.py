import asyncio

async def compute(x, wait=2):
    print("Compute:",x)
    await asyncio.sleep(wait)
    return x**2+1

async def run():
    y = await compute(3, wait=3)
    print(y)

asyncio.run(run())