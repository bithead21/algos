import asyncio
import aiohttp
from time import sleep

"""
Concurent tasks
"""

async def task(name):
    print(f"running task {name}")
    await asyncio.sleep(4)
    print(f"task {name} finished.")

async def impl():
    t1 = asyncio.create_task(task("A"))
    t2 = asyncio.create_task(task("B"))
    await t1
    await t2

"""
Concurent http requests with (aiohttp)
"""

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            res = await resp.text()
            print(f"[{url}] [GET] resp_len={len(res)}")

async def core():
    urls = ["https://python.org", "https://example.com"]
    tasks = [asyncio.create_task(fetch_url(url)) for url in urls]
    await asyncio.wait(tasks)
