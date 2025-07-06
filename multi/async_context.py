import asyncio

class async_ctx:
    async def __aenter__(self):
        print("enter")
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("exit")


async def main():
    async with async_ctx() as ctx:
        print("ctx...")

asyncio.run(main())