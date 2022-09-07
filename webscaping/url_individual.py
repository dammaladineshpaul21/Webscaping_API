import re
from bs4 import BeautifulSoup
import requests
import itertools
import time
import asyncio
import aiohttp


async def get_all_urls(url):
    """GET all the link in the Website"""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, ssl=False) as requs:
                soup = BeautifulSoup(await requs.text(), 'html.parser')
        # soup = BeautifulSoup(requests.get(url).text, 'html.parser')
        urls = [link.get('href') for link in soup.find_all('a')]
        urls_contact = [i for i in set([get_specific_url for get_specific_url in set(urls) \
                                        if "location" in str(get_specific_url) or "contact" in str(get_specific_url) \
                                        or "about" in str(get_specific_url) \
                                        or "facebook" in str(get_specific_url) \
                                        or "main" in str(get_specific_url)])]

        if len([i for i in urls_contact if re.compile("^[a-z]|/").findall((str(i)))]) >= 1:
            get_d = [None if re.compile(f"http").findall(str(i)) or re.compile(f"/").findall(str(i)) else "/" + i
                     for i in urls_contact]
            # if re.compile(f"http").findall(str(i)):
            #     pass
            # else:
            #     get_d.append(i)
            urls_contact2 = [str(url) + "/" + str(i[1::]) for i in itertools.chain(urls_contact, get_d) \
                             if str(i).startswith("/")]
            get_filter_urls = [i for i in list(map(lambda i: i if str(i).startswith("http") else None,
                                                   itertools.chain(urls_contact, urls_contact2))) \
                               if i is not None]
            get_full_filter_url = [url] + get_filter_urls
            await asyncio.sleep(0.10)
            return get_full_filter_url
        else:
            get_full_filter_url = [url] + urls_contact
            await asyncio.sleep(0.25)
            return get_full_filter_url
    except Exception:
        return f"Invalide URL as been assigned to function [get_the_urls]"


async def get_all_text(get_all_urls):
    """Will Execute all the text retived from the ULR"""
    store_number_info = []
    soup = [BeautifulSoup(requests.get(txt).text, 'html.parser') for txt in await get_all_urls]
    pattern = re.compile(r"[A-Z0-9a-z'&a-z0-9]+|@|!|-|'|#|&|%")
    get_num = pattern.findall(str(soup).strip(), re.LOCALE)
    store_number_info.append(get_num)
    # comdine_text_value = set([j for i in store_number_info for j in i])
    comdine_text_value = [j for i in store_number_info for j in i]
    # comdine_text_value.union(self.extract_the_copyrights())
    await asyncio.sleep(0.5)
    return comdine_text_value


def get_patter_verificaiton(user_name):
    name = user_name.split()
    if re.compile("@|!|#|-|&|%").findall(" ".join(name)):
        name1 = [" ".join(j) for j in [name[0:i + 1] for i in range(len(name))][0:len(name)][0:len(name) - 1]]
        get_filter_name = [[i for i in name1 if re.compile("@|!|-|#|&|%").findall(i)][0]]
        return get_filter_name
    else:
        pass

