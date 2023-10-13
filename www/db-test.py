import asyncio

from www.models import User
from www.orm import create_pool


async def test():
    loop = asyncio.get_event_loop()
    # Specify the connection parameters in the kwargs dictionary
    db_config = {
        'user': 'root',
        'password': 'changyou',
        'db': 'awesome-blog-prod',
        # 'host': 'your_host',
    }
    loop.run_until_complete(create_pool(loop, **db_config))
    # await create_pool(loop, **db_config)
    # await create_pool(user='root', password='changyou', db='awesome-blog-prod')  # Use await here

    u = User(name='changyou', email='changyou0730@163.com', passwd='changyou', image='about:blank')
    await loop.run_until_complete(u.save())
    # await u.save()  # Use await here

async def main():
    # Create an event loop
    loop = asyncio.get_event_loop()
    # Call the asynchronous test function within the event loop
    await test()

if __name__ == '__main__':
    asyncio.run(main())  # Run the event loop
