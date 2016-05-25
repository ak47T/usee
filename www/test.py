# import sys
import orm
import asyncio
from models import User, Blog, Comment


def test(loop):
    yield from orm.create_pool(loop=loop,user='www-data', password='www-data', db='awesome')

    u = User(name='Test55', email='test78@example.com', passwd='1253', image='blank')

    yield from u.save()


	
loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
# if __name__ == '__main__':

    # loop = asyncio.get_event_loop()
    # loop.run_until_complete( asyncio.wait([test( loop )]) )  
    # loop.close()
    # if loop.is_closed():
    #     sys.exit(0)
# for x in test():
#     pass