import asyncio

async def watch(name):
    print(f"Watching {name}...")
    await asyncio.sleep(2)
    print(f"Finished watching {name}.")

async def main():
    await asyncio.gather(
        watch("Aladdin"),
        watch("Transformers"),
        watch("Iron man"),
    )

asyncio.run(main())


""" 
Explanation: 
In this code, we define an asynchronous function `watch` that simulates watching a movie by printing a message,
waiting for 2 seconds, and then printing another message.
The `main` function uses `asyncio.gather` to run multiple instances of the `watch` function concurrently for different movies.
All functions are executed concurrently, so the output will be:

Watching Aladdin...
Watching Transformers...
Watching Iron man...
Finished watching Aladdin.
Finished watching Transformers.
Finished watching Iron man. 

If we were to run the watch function sequentially, the output would be:
Watching Aladdin...
Finished watching Aladdin.      
Watching Transformers...
Finished watching Transformers.    
Watching Iron man...
Finished watching Iron man.
"""
    