import asyncio
import re
import time

import aiohttp
from bs4 import BeautifulSoup


async def phone_number_string(url):
    try:
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=6)) as session:
            async with session.get(url, ssl=True) as requs:
                soup = BeautifulSoup(await requs.text(), 'html.parser')
            await session.close()
            number_extraction = [i for i in
                                 list(map(lambda x: x if len(x) > 1 else None, re.findall(r"[0-9]+", str(soup)))) \
                                 if i is not None]
            await asyncio.sleep(0.05)
            return " ".join(number_extraction).replace(" ", "")
    except Exception as e:
        await asyncio.sleep(0.5)
        return e




# async def main():
#     stor_val = []
#     for i in range(len(urls)):
#         task_1 = asyncio.create_task(phone_number_string(urls[i]))
#         stor_val.append(await task_1)
#     return stor_val
#
# str_tm = time.time()
# print(asyncio.run(main()))
# end_tm = time.time()
# print(end_tm - str_tm)
