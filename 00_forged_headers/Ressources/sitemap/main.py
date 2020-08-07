from bs4 import BeautifulSoup
import aiohttp
import asyncio


async def run():
    url = "http://192.168.0.35/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            soup = BeautifulSoup(await resp.text(), features="html.parser")
            for ref in soup.find_all('a', href=True)[1:]:
                print(ref["href"])

if __name__ == '__main__':
    asyncio.run(run())
