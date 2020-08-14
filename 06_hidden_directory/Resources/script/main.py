from bs4 import BeautifulSoup
import aiohttp
import asyncio
import re
import time
import math


async def scrape(response):
    soup = BeautifulSoup(await response.text(), features="html.parser")
    for ref in reversed(soup.find_all('a', href=True)[1:]):
        url = str(response.url) + ref['href']
        if ref['href'] == 'README':
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    if re.search('^\S*$', await resp.text()):
                        print(f"{url}\n{await resp.text()}")
                        return True
        else:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    if await scrape(resp):
                        return True
    return False


async def run():
    start = time.time()
    url = "http://192.168.0.35/.hidden/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            await scrape(resp)
    stop = time.time()
    print(
        f"Runtime: "
        f"{math.floor((stop - start) / 60)} minutes "
        f"{math.floor((stop - start) % 60)} seconds"
    )

if __name__ == '__main__':
    asyncio.run(run())
