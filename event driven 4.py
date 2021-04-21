#PROCESSING RANDOM TASKS
import asyncio
import time
async def Task_ex(n):
   time.sleep(1)
   print("Processing {}".format(n))
async def Generator_task():
   for i in range(10):
      asyncio.ensure_future(Task_ex(i))
   int("Tasks Completed")
   asyncio.sleep(2)

loop = asyncio.get_event_loop()
loop.run_until_complete(Generator_task())
loop.close()
#CODE BY AYUSH SAXENA