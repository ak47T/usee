import sys
import orm
import asyncio
from models import User, Blog, Comment


def test(loop):
    yield from orm.create_pool(user='www-data', password='www-data', db='awesome',loop=loop)

    u = User(id='123',name='Test2', email='test2@example.com', passwd='1253', image='blank')

    yield from u.save()

	
# loop = asyncio.get_event_loop()
# loop.run_until_complete(test())
# loop.close()
if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.run_until_complete( asyncio.wait([test( loop )]) )  
    loop.close()
    if loop.is_closed():
        sys.exit(0)
# for x in test():
#     pass