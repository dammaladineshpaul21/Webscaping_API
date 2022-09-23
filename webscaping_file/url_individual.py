import re
from bs4 import BeautifulSoup
import requests
import itertools
import asyncio
import aiohttp
import urllib3

urllib3.disable_warnings()


async def get_all_urls(url):
    """GET all the link in the Website"""
    if url[-1] == "/":
        url = "".join([url[i] for i in range(len(url) - 1)])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, ssl=True) as requs:
                soup = BeautifulSoup(await requs.text(), 'html.parser')
            await session.close()
        urls = [link.get('href') for link in soup.find_all('a')]
        urls_contact = [i for i in set([get_specific_url for get_specific_url in set(urls)
                                        if "location" in str(get_specific_url)
                                        or "contact" in str(get_specific_url)
                                        or "about" in str(get_specific_url)
                                        or "store" in str(get_specific_url)
                                        or "main" in str(get_specific_url)
                                        or "facebook" in str(get_specific_url)
                                        or "instagram" in str(get_specific_url)
                                        or "yelp" in str(get_specific_url)
                                        or "tripadvisor" in str(get_specific_url)])]

        if len([i for i in urls_contact if re.findall("^[a-z]|/", (str(i)))]) >= 1:
            get_d = [None if re.findall(r"http", str(i)) or re.findall(r"/", str(i)) else "/" + i
                     for i in urls_contact]
            urls_contact2 = [str(url) + "/" + str(i[1::]) for i in itertools.chain(urls_contact, get_d)
                             if str(i).startswith("/")]
            get_filter_urls = [i for i in list(map(lambda i: i if str(i).startswith("http") else None,
                                                   itertools.chain(urls_contact, urls_contact2)))
                               if i is not None]
            get_full_filter_url = [url] + get_filter_urls
            await asyncio.sleep(0.50)
            return get_full_filter_url
        else:
            get_full_filter_url = [url] + urls_contact
            await asyncio.sleep(0.5)
            return get_full_filter_url
    except Exception as e:
        return f"Invalid URL Provided By the user at {url} and {e}"


async def get_all_text(all_urls):
    """Will Execute all the text retived from the ULR"""
    get_filter_url = [i for i in all_urls if not re.findall(r"facebook|instagram|location", i)]
    store_number_info = []
    soup = [BeautifulSoup(requests.get(txt, verify=False).text, 'html.parser') for txt in get_filter_url]
    get_string = re.findall(r"[A-Za-z\w'a-z-&A-Za-z]+|[0-9]+", str(soup).strip())
    get_num = re.findall(r"[0-9]+", str(soup).strip())
    store_number_info.append(get_string)
    comdine_text_value = [j for i in store_number_info for j in i]
    await asyncio.sleep(0.20)
    return comdine_text_value, get_num

