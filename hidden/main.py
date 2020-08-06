from bs4 import BeautifulSoup
import aiohttp
import asyncio
import re
import time
import math


async def read_me(url, start):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if re.search('^\S*$', await resp.text()):
                stop = time.time()
                print(
                    f"{url}\n"
                    f"{await resp.text()}"
                    f"Runtime: "
                    f"{math.floor((stop - start) / 60)} minutes "
                    f"{math.floor((stop - start) % 60)} seconds"
                )
                exit(0)


async def scrape(response, start):
    soup = BeautifulSoup(await response.text(), features="html.parser")
    for a_tag in reversed(soup.find_all('a', href=True)[1:]):
        url = str(response.url) + a_tag['href']
        if a_tag['href'] == 'README':
            await read_me(url, start)
        else:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    await scrape(resp, start)


async def run():
    start = time.time()
    url = "http://192.168.0.35/.hidden/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            await scrape(resp, start)


if __name__ == '__main__':
    asyncio.run(run())
