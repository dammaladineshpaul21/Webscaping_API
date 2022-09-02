import re
from bs4 import BeautifulSoup
import requests
import itertools
import numpy as np


def get_all_urls(url):
    """GET all the link in the Website"""
    try:
        soup = BeautifulSoup(requests.get(url).content, 'html.parser')
        urls = [link.get('href') for link in soup.find_all('a')]
        urls_contact = [i for i in set([get_specific_url for get_specific_url in set(urls) \
                                        if "location" in str(get_specific_url) or "contact" in str(get_specific_url) \
                                        or "about" in str(get_specific_url) \
                                        or "facebook" in str(get_specific_url) \
                                        or "main" in str(get_specific_url)])]

        if len([i for i in urls_contact if re.compile("^[a-z]").findall((str(i)))]) >= 1:
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
            return get_full_filter_url
        else:
            get_full_filter_url = [url] + urls_contact
            return get_full_filter_url
    except Exception:
        return f"Invalide URL as been assigned to function [get_the_urls]"


def get_all_text(get_all_urls):
    """Will Execute all the text retived from the ULR"""
    # str_time = time.time()
    store_number_info = []
    # for txt in self.get_all_urls():
    soup = [BeautifulSoup(requests.get(txt).text, 'html.parser') for txt in get_all_urls]
    pattern = re.compile(r"[A-Za-z]+")
    get_num = pattern.findall(str(np.array(soup)))
    store_number_info.append(get_num)
    # comdine_text_value = set([j for i in store_number_info for j in i])
    comdine_text_value = [j for i in store_number_info for j in i]
    # comdine_text_value.union(self.extract_the_copyrights())
    # end_time = time.time()
    return comdine_text_value



