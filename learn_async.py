import asyncio

async def get_name(name):
  if (name == "1 m"):
    await custom_sleep()
  await count()
  print(name)
 
async def count():
  for x in range(0, 10):
    print(x)
    
async def custom_sleep():
  await asyncio.sleep(5)

loop = asyncio.get_event_loop()
tasks = [  
    asyncio.ensure_future(get_name("1 m")),
    asyncio.ensure_future(get_name("2 m")),
]

loop.run_until_complete(asyncio.wait(tasks)) 
loop.close()
