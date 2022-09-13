import re
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
    try:
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=5)) as session:
            async with session.get(url, ssl=True) as requs:
                soup = BeautifulSoup(await requs.text(), 'html.parser')
            await session.close()
        urls = [link.get('href') for link in soup.find_all('a')]
        urls_contact = [i for i in set([get_specific_url for get_specific_url in set(urls) \
                                        if "location" in str(get_specific_url) or "contact" in str(get_specific_url) \
                                        or "about" in str(get_specific_url) \
                                        or "facebook" in str(get_specific_url) \
                                        or "main" in str(get_specific_url)])]

        if len([i for i in urls_contact if re.compile("^[a-z]|/").findall((str(i)))]) >= 1:
            get_d = [None if re.compile(f"http").findall(str(i)) or re.compile(f"/").findall(str(i)) else "/" + i
                     for i in urls_contact]
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
    except Exception as e:
        return e


async def get_all_text(get_all_urls):
    """Will Execute all the text retived from the ULR"""
    store_number_info = []
    soup = [BeautifulSoup(requests.get(txt, verify=False).text, 'html.parser') for txt in await get_all_urls]
    pattern = re.compile(r"[A-Za-z\w'a-z-&A-Za-z'a-z]+")
    get_num = pattern.findall(str(soup).strip())
    store_number_info.append(get_num)
    comdine_text_value = [j for i in store_number_info for j in i]
    await asyncio.sleep(0.10)
    return comdine_text_value


async def mixed_name(name, get_all_text):
    get_correct_name = []
    for i in range(len(name)):
        if re.compile(str(name[i]).replace(" ", "").lower()).findall(" ".join(get_all_text)):
            get_correct_name.append(name[i])
        else:
            pass
    await asyncio.sleep(0.25)
    return get_correct_name


async def check_spacial_case(name, file_pass):
    with open(file_pass) as file:
        get_data = json.load(file)
        create_df = pd.DataFrame(get_data, columns=["character", "letter_convertion"])
        make_table = create_df.set_index("character").to_dict()
        get_sp_char = [i for i, k in make_table["letter_convertion"].items()]
        if "&" not in name:
            for val in name.split():
                get_val = [i for i in [None if re.compile(r"[A-Za-z]").findall(i) else i for i in val] if i is not None]
                get_final_Re = [i for i in list(itertools.chain(*[list(map(lambda x: x if get_val[i] in x else None, \
                                                                           get_sp_char)) for i in range(len(get_val))]))
                                if i is not None]
                for i in range(len(get_final_Re)):
                    name = name.replace(name[name.index(get_val[i])], make_table["letter_convertion"][get_final_Re[i]])
            await asyncio.sleep(0.25)
            return name
        elif "’" in name:
            name = name.replace(name[name.index("’")], make_table["letter_convertion"]["’"])
            return name
        else:
            name = name.replace(name[name.index("&")], make_table["letter_convertion"]["&"])
            await asyncio.sleep(0.10)
            return name


def site_varification(get_text, error_massage):
    get_result = [i for i in list(map(lambda x: x if re.compile(x).findall(get_text) else None, error_massage)) if
                  i is not None]
    return get_result


def get_all_val(incorrect_val, top_name_incorrect, match, no_match, error_code):
    return dict(Incorrect_val=incorrect_val, top_name_incorrect=top_name_incorrect,
                match=match, no_match=no_match, error_code=error_code)


async def error_check(get_all_urls):
    """Will Execute all the text retived from the ULR"""
    store_number_info = []
    soup = BeautifulSoup(requests.get(get_all_urls, verify=False).text, 'html.parser')
    pattern = re.compile(r"[A-Za-z\w'a-z-&A-Za-z'a-z]+")
    get_num = pattern.findall(str(soup).strip())
    store_number_info.append(get_num)
    comdine_text_value = [j for i in store_number_info for j in i]
    await asyncio.sleep(0.10)
    return comdine_text_value


def extract_the_copyrights(url):
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    get_name = []
    for tag in soup.findAll(text=re.compile(r'©|copy;')):
        copyrighttexts = tag.parent.text
        get_name.append(copyrighttexts)
    get_name.append(soup.title.string)
    return [get_name[0].strip()]


# async def main(url):
#     # try:
#     #     l = await asyncio.wait_for(asyncio.gather(error_check(url)), timeout=4.0)
#     #     print(l)
#     # except asyncio.TimeoutError:
#     #     print("Time Out Error")
#     l = await asyncio.gather(asyncio.to_thread(asyncio.run(error_check(url))))
#     print(l)
#
# asyncio.run(main("http://vuedemer.fr"))
