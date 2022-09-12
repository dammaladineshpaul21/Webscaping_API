import re
import pandas as pd
from bs4 import BeautifulSoup
import requests
import itertools
import time
import asyncio
import aiohttp
import json
from urllib import parse


async def get_all_urls(url):
    """GET all the link in the Website"""
    try:
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=5)) as session:
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
    except Exception as e:
        return e


async def get_all_text(get_all_urls):
    """Will Execute all the text retived from the ULR"""
    store_number_info = []
    soup = [BeautifulSoup(requests.get(txt).text, 'html.parser') for txt in await get_all_urls]
    pattern = re.compile(r"[A-Z'0-9a-z'&a-z'0-9]+|@|!|-|'|#|&|%")
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


async def mixed_name(name, get_all_text):
    get_correct_name = []
    for i in range(len(name)):
        if re.compile(str(name[i]).replace(" ", "").lower()).findall(" ".join(get_all_text)):
            get_correct_name.append(name[i])
        else:
            pass
    await asyncio.sleep(0.50)
    return get_correct_name


async def check_spacial_case(name, file_pass):
    with open(file_pass) as file:
        get_data = json.load(file)
        create_df = pd.DataFrame(get_data, columns=["character", "letter_convertion"])
        make_table = create_df.set_index("character").to_dict()
        get_sp_char = [i for i, k in make_table["letter_convertion"].items()]
        for val in name.split():
            get_val = [i for i in [None if re.compile(r"[A-Za-z]").findall(i) else i for i in val] if i is not None]
            get_final_Re = [i for i in list(itertools.chain(*[list(map(lambda x: x if get_val[i] in x else None, \
                                                                       get_sp_char)) for i in range(len(get_val))])) if
                            i is not None]
            for i in range(len(get_final_Re)):
                name = name.replace(name[name.index(get_val[i])], make_table["letter_convertion"][get_final_Re[i]])
        await asyncio.sleep(0.25)
        return name

        # get_name_split = name.split(" ")
        # for k in range(len(get_name_split)):
        #     # get_val = [None if re.compile(r"[A-Za-z]").findall(i) else i for i in name[k]]
        #     get_val = " ".join([i for i in list(map(lambda x: None if re.compile(r"[A-Za-z]").findall(x) else x,
        #                                             get_name_split[k].strip())) if i is not None]).strip()
        #
        #     store_sp_chr.append(get_val)
        # get_key_phase = list(itertools.chain(
        #     *[[i for i in map(lambda x: x if store_sp_chr[i] in x else None, get_sp_char) if i is not None] \
        #       for i in range(len(store_sp_chr))]))
        # for i in range(len(get_name_split)):
        #     filted_name.append(get_name_split[i].replace(get_name_split[i][get_name_split[i].index(store_sp_chr[i])],\
        #                                                  make_table["letter_convertion"][get_key_phase[i]]))
        # return store_sp_chr


def site_varification(get_text, error_massage):
    get_result = [i for i in list(map(lambda x: x if re.compile(x).findall(get_text) else None, error_massage)) if
                  i is not None]
    return get_result


# async def main():
#     task_1 = asyncio.create_task(get_all_urls("https://rackys.co.uk"))
#     task_2 = asyncio.create_task(get_all_text(task_1))
#     await task_1
#     task1 = await task_2
#     print(" ".join(task1))
#
#
# asyncio.ru