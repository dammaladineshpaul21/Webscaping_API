import re
import time
from bs4 import BeautifulSoup
import requests
import itertools
import asyncio
import aiohttp
import urllib3
from numba import jit

urllib3.disable_warnings()


def time_it(fun):
    def inner_fun(*args, **kwargs):
        str_time = time.perf_counter()
        fun(*args, **kwargs)
        end_time = time.perf_counter()
        return f"{end_time - str_time}"

    return inner_fun

@time_it
def get_all_urls(url):
    """GET all the link in the Website"""
    if url[-1] == "/":
        url = "".join([url[i] for i in range(len(url) - 1)])
    try:
        async def activet_url(url):
            async with aiohttp.ClientSession() as session:
                async with session.get(url, ssl=True, timeout=7) as requs:
                    if requs.status == 200:
                        soup = BeautifulSoup(await requs.text(), 'html.parser')
                await session.close()
                return soup

        urls = [link.get('href') for link in asyncio.run(activet_url(url)).find_all('a')]
        urls_contact = [i for i in set([get_specific_url
                                        for get_specific_url in set(urls)
                                        if re.findall(
                "location|contact|about|store|main|facebook|instagram|yelp|tripadvisor", get_specific_url)])]

        if len([i for i in urls_contact if re.findall("^[a-z]|/", (str(i)))]) >= 1:
            get_d = [None if re.findall(r"http", str(i)) or re.findall(r"/", str(i)) else "/" + i
                     for i in urls_contact]
            urls_contact2 = [str(url) + "/" + str(i[1::]) for i in itertools.chain(urls_contact, get_d)
                             if str(i).startswith("/")]
            get_filter_urls = [i for i in list(map(lambda i: i if str(i).startswith("http") else None,
                                                   itertools.chain(urls_contact, urls_contact2)))
                               if i is not None]
            get_full_filter_url = [url] + get_filter_urls
            return get_full_filter_url
        else:
            get_full_filter_url = [url] + urls_contact
            return get_full_filter_url
    except Exception as e:
        return f"Invalid URL Provided By the user at {url} and {e}"


@time_it
def get_all_text(all_urls):
    try:
        """Will Execute all the text retived from the ULR"""
        get_filter_url = [i for i in all_urls if not re.findall(r"instagram|yelp|tripadvisor", i)]
        store_number_info = []
        soup = [BeautifulSoup(requests.get(txt).text, 'html.parser') for txt in get_filter_url]
        get_string = re.findall(r"[A-Za-z\wa-z-&A-Za-z]+|[0-9]+", str(soup).strip())
        get_num = re.findall(r"[0-9]+", str(soup).strip())
        store_number_info.append(get_string)
        comdine_text_value = [j for i in store_number_info for j in i]
        time.sleep(1)
        return comdine_text_value, get_num
    except Exception as e:
        return e


get_v = jit()(get_all_urls)
get_l = jit()(get_all_text)

print(get_all_urls("http://www.skatelescope.org"))
