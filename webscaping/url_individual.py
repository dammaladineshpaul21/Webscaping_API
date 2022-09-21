import re
import time

import pandas as pd
from bs4 import BeautifulSoup
import requests
import itertools
import asyncio
import aiohttp
import json
import urllib3

urllib3.disable_warnings()


async def get_all_urls(url):
    """GET all the link in the Website"""
    if url[-1] == "/":
        url = "".join([url[i] for i in range(len(url) - 1)])
    try:
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=5)) as session:
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
        return e


# async def extract_social_mediapage(get_all_urls):
#     get_socialmedia = [i for i in get_all_urls if "facebook" in i or "instagram" in i]
#     get_third_party = [i for i in get_all_urls if "yelp" in i or "tripadvisor" in i]
#     await asyncio.sleep(0.25)
#     return json.dumps(str(get_socialmedia)), json.dumps(str(get_third_party))


async def get_all_text(get_all_urls):
    """Will Execute all the text retived from the ULR"""
    get_filter_url = [i for i in get_all_urls if not re.findall(r"contact|facebook|instagram|location", i)]
    store_number_info = []
    soup = [BeautifulSoup(requests.get(txt, verify=False).text, 'html.parser') for txt in get_filter_url]
    get_string = re.findall(r"[A-Za-z\w'a-z-&A-Za-z]+|[0-9]+", str(soup).strip())
    get_num = re.findall(r"[0-9]+", str(soup).strip())
    # get_num = re.findall(r"[0-9]+", str(soup).strip())
    store_number_info.append(get_string)
    comdine_text_value = [j for i in store_number_info for j in i]
    comdine_num_value = [j for i in store_number_info for j in i]
    task_1 = asyncio.create_task(error_check(get_all_urls[0]))
    await task_1
    await asyncio.sleep(0.20)
    return comdine_text_value, get_num


async def error_check(get_all_urls):
    """Will Execute all the text retived from the ULR"""
    try:
        # async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=2)) as session:
        #     async with session.get(get_all_urls, ssl=True) as requs:
        #         soup = BeautifulSoup(await requs.text(), 'html.parser')
        #     await session.close()
        soup = BeautifulSoup(requests.get(get_all_urls).text, 'html.parser')
        store_number_info = []
        get_num = re.findall(r"[A-Za-z\w'a-z-&A-Za-z'a-z]+", str(soup).strip())
        store_number_info.append(get_num)
        comdine_text_value = [j for i in store_number_info for j in i]
        await asyncio.sleep(0.20)
        return comdine_text_value
    except Exception as e:
        return f"URL Connection Error {e}"


async def mixed_name(name, get_all_text):
    try:
        get_correct_name = []
        for i in range(len(name)):
            if re.findall(str(name[i]).replace(" ", "").lower(), " ".join(get_all_text)):
                get_correct_name.append(name[i])
            else:
                pass
        await asyncio.sleep(0.4)
        return get_correct_name
    except Exception:
        return dict(error_massage=ValueError)


async def check_spacial_case(name, file_pass):
    try:
        with open(file_pass) as file:
            get_data = json.load(file)
            create_df = pd.DataFrame(get_data, columns=["character", "letter_convertion"])
            make_table = create_df.set_index("character").to_dict()
            get_sp_char = [i for i, k in make_table["letter_convertion"].items()]
            if "&" not in name:
                for val in name.split():
                    get_val = [i for i in [None if re.findall(r"[A-Za-z]", i) else i for i in val] if
                               i is not None]
                    get_final_Re = [i for i in list(itertools.chain(*[list(map(lambda x: x if get_val[i] in x else None,
                                                                               get_sp_char)) for i in
                                                                      range(len(get_val))]))
                                    if i is not None]
                    for i in range(len(get_final_Re)):
                        name = name.replace(name[name.index(get_val[i])],
                                            make_table["letter_convertion"][get_final_Re[i]])
                await asyncio.sleep(0.75)
                return name
            elif "’" in name:
                name = name.replace(name[name.index("’")], make_table["letter_convertion"]["’"])
                await asyncio.sleep(0.5)
                return name
            else:
                name = name.replace(name[name.index("&")], make_table["letter_convertion"]["&"])
                await asyncio.sleep(0.5)
                return name
    except Exception:
        return ValueError


async def site_varification(get_text):
    error_massage = ["HTTP Error 503", "404 forbidden", "404 Not Found", "Error 404 - Page Not Found",
                     "Domain for Sale", "Mod_Security"
                                        "404 Error Pages", "errorCode 1020", "403 Forbidden",
                     "Error Page cannot be displayed", "Domain Not Claimed", "This domain is for sale"]
    try:
        get_result = [i for i in list(map(lambda x: x if re.findall(x, get_text) else None, error_massage)) if
                      i is not None]
        await asyncio.sleep(0.5)
        return get_result
    except Exception:
        return ValueError


def get_all_val(incorrect_val, top_name_incorrect, match, no_match,
                error_code):
    try:
        return dict(Incorrect_val=incorrect_val, top_name_incorrect=top_name_incorrect,
                    match=match, no_match=no_match, error_code=error_code)
    except Exception:
        return AttributeError


def extract_the_copyrights(url):
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    get_name = []
    for tag in soup.findAll(text=re.compile(r'©|copy;')):
        copyrighttexts = tag.parent.text
        get_name.append(copyrighttexts)
    get_name.append(soup.title.string)
    return [get_name[0].strip()]


loop = asyncio.get_event_loop()

# print(loop.run_until_complete(get_all_urls("https://www.caautoglassf.com")))
# print(asyncio.run(get_all_text(loop.run_until_complete(get_all_urls("https://manchesterartgallery.org"))[0])))
# # print(error_check(loop.run_until_complete(get_all_urls("https://manchesterartgallery.org"))))
# print(asyncio.run(site_varification("403 Forbidden")))
