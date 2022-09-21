import asyncio
import re
import aiohttp
from bs4 import BeautifulSoup


async def phone_number_string(url):
    """Get the URL from the payload and extracts are the number
    and make's it into a string."""
    try:
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=6)) as session:
            async with session.get(url, ssl=True) as requs:
                soup = BeautifulSoup(await requs.text(), 'html.parser' or 'lxml')
            await session.close()
            number_extraction = [i for i in
                                 list(map(lambda x: x if len(x) > 1 else None,
                                          re.findall(r"[0-9]+", str(soup).replace(" ", ""))))
                                 if i is not None]
            await asyncio.sleep(0.05)
            return number_extraction
    except Exception as e:
        await asyncio.sleep(0.5)
        return e


async def get_ow_number(url):
    try:
        """All the Required Pattern related to Phone_number based on the url provided
        and check the pattern associated with it."""
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=6)) as session:
            async with session.get(url, ssl=True) as requs:
                soup = BeautifulSoup(await requs.text(), 'html.parser')
            await session.close()
            phone_pattern = [r"\d{3}\W\d{3}\W\d{4}/\d{4}", r"\(\d{3}\) \d{3}-\d{4}",
                             r"\d{3}\W\d{3}\W\d{4}|\d{1}-\d{3}-\d{3}-\d{4}"]
            store_phone_number = []
            for i in range(len(phone_pattern)):
                if re.findall(phone_pattern[i], str(soup)):
                    store_phone_number.append(list(set(re.findall(phone_pattern[i], str(soup)))))
            await asyncio.sleep(0.5)
            return store_phone_number
    except Exception as e:
        await asyncio.sleep(0.5)
        return e


async def get_number_list(numbers_list):
    """Get the individul number provided in the payload
    and filter all the Spacial Character from the single number the
    and give a raw string of only containing number."""
    try:
        filter_number = re.findall(r"[0-9]+", numbers_list)
        await asyncio.sleep(0.0)
        return " ".join(filter_number).replace(" ", "")
    except Exception as e:
        await asyncio.sleep(0.0)
        return e
