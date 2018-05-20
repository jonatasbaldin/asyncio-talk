import asyncio
import time


async def task_one():
    print('> Starting task_one')
    asyncio.sleep(2)
    print('> Finish task_one')


async def task_two():
    print('> Starting task_two')
    asyncio.sleep(2)
    print('> Finish task_two')


async def main():
    await task_one()
    await task_two()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
