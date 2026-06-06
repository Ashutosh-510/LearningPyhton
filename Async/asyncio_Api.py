import asyncio 
import aiohttp

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()
         
async def main():
    urls = [
        "https://www.example.com",
        "https://www.python.org",
        "https://www.asyncio.org"
    ]
    
    tasks = [fetch_url(url) for url in urls]
    results = await asyncio.gather(*tasks)
    
    
asyncio.run(main())