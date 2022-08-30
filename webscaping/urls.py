import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import nltk
import json
import numpy as np
import itertools

# class Url_object_main:
#
#     def __init__(self, read_file):
#         with open(read_file) as file:
#             get_read_file = json.load(file)
#             # self.read_file = get_read_file["urls"]
#             self.read_file = get_read_file["urls"][0]["url1"]
#
#     try:
#         def get_date_file_values(self):
#             return self.read_file
#     except Exception:
#         raise f"{WindowsError} Page Was not working"


class URLs_info():

    def __init__(self, urls):
        self.urls = urls

    def get_access(self):
        """This fucntion extract the title name in the Official Website"""
        try:
            if requests.get(self.urls).status_code == 200:
                try:
                    # making requests instance
                    reqs = requests.get(self.urls)
                    return reqs
                except Exception as err:
                    return err
            else:
                print("The given URL is Broken. or URL's shoud be removed or POI has been closed")
        except Exception as err:
            return f"Something went wrong in funciotn {id(self.get_access)}{err}"

    def extract_the_copyrights(self):
        urls = self.urls
        webpage = requests.get(urls)
        soup = BeautifulSoup(webpage.content, 'html.parser')
        get_name = []
        for tag in soup.findAll(text=re.compile(r'©|copy;')):
            copyrighttexts = tag.parent.text
            get_name.append(copyrighttexts)
        get_name.append(soup.title.string)
        return get_name[0].strip()

    def get_all_urls(self):
        """GET all the link in the Website"""
        try:
            soup = BeautifulSoup(requests.get(self.urls).content, 'html.parser')
            urls = [link.get('href') for link in soup.find_all('a')]
            urls_contact = [i for i in set([get_specific_url for get_specific_url in set(urls) \
                                if "location" in str(get_specific_url) or "contact" in str(get_specific_url) \
                                or "about" in str(get_specific_url) \
                                or "main" in str(get_specific_url)])]
            pattern = re.compile(r"^[a-z]")
            if len([i for i in urls_contact if re.compile("^/").findall((str(i)))]) >= 1:
                get_d = ["/" + i for i in urls_contact if pattern.findall(str(i))]
                urls_contact2 = [str(self.urls)+"/"+str(i[1::]) for i in itertools.chain(urls_contact,get_d) \
                             if str(i).startswith("/")]
                get_filter_urls = [i for i in list(map(lambda i: i if str(i).startswith("http") else None, itertools.chain(urls_contact, urls_contact2))) \
                                   if i is not None]
                get_full_filter_url = [self.urls] + get_filter_urls
                return get_full_filter_url
            else:
                get_full_filter_url = [self.urls] + urls_contact
                return get_full_filter_url
        except Exception:
            return f"Invalide URL as been assigned to function [get_the_urls]"

    def get_all_values(self):
        try:
            get_abt_home_main_page, get_all_location_page = [], []
            for i in self.get_all_urls():
                if "about" in i or "contact" in i or "contact-us" in i or "find-us" in i or "find" in i:
                    get_abt_home_main_page.append(i)
                elif "location" in i:
                    get_all_location_page.append(i)
                else:
                    pass
            # using the BeautifulSoup module
            store_url_text_info = []
            for urlinfo in get_abt_home_main_page:
                soup = BeautifulSoup(requests.get(urlinfo).text, 'html.parser')
                # displaying the title
                # get_txt = [title.strip() for title in soup.text.split()]
                for title in soup.text.split():
                    store_url_text_info.append(title)
            return set(store_url_text_info), get_all_location_page
        except Exception as err:
            raise f"Values Has been not generated for URL {err}"

    def get_number(self):
        """Get the DATA from the URL """
        try:
            store_number_info = []
            for txt in self.get_all_urls():
                soup = BeautifulSoup(requests.get(txt).text, 'html.parser')
                pattern = re.compile(r"\d+")
                get_num = pattern.findall(str(soup))
                store_number_info.append(get_num)
            combine_number_val = set([j for i in store_number_info for j in i])
            return combine_number_val
        except Exception as err:
            return f"Number Has been not generated for URL {err}"

    def get_all_text(self):
        """Will Execute all the text retived from the ULR"""
        store_number_info = []
        for txt in self.get_all_urls():
            soup = BeautifulSoup(requests.get(txt).text, 'html.parser')
            pattern = re.compile(r"[A-Za-z]+")
            get_num = pattern.findall(str(soup))
            store_number_info.append(get_num)
        comdine_text_value = set([j for i in store_number_info for j in i])
        return comdine_text_value

    def get_phonenumber(self):
        store_number_info = []
        for txt in self.get_all_urls():
            soup = BeautifulSoup(requests.get(txt).content, 'html.parser')
            pattern = re.compile(r"\(\d{3}\)|\d{3}-\d{4}|\d{3} \d{4}")
            get_num = pattern.findall(str(soup))
            store_number_info.append(get_num)
        comdine_phonenumber_value = set([j for i in store_number_info for j in i])
        return comdine_phonenumber_value

    def get_category(self):
        with open("../resources_file/category.json") as file:
            get_data = json.load(file)
            create_df = pd.DataFrame(get_data, columns=['alias', "title"])
            category_dict = create_df.set_index("alias").to_dict()
            # category_dict["parents"]
            is_noun = lambda pos: pos[:2] == 'NN'
            # do the nlp stuff
            tokenized = nltk.word_tokenize(str(self.get_all_text()))
            nouns = [word[1:] for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
            store_category_parents = []
            for i in nouns:
                try:
                    store_category_parents.append(category_dict['title'][i])
                except KeyError:
                    pass

            return f"Missing/Updating Category {store_category_parents}"

url_object = URLs_info("https://www.lepaindenosancetres.com")
print(url_object.get_all_text())