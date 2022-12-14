# import asyncio
# import multiprocessing
# import requests
# from bs4 import BeautifulSoup
# import re
# import pandas as pd
# import nltk
# import json
# import numpy as np
# import itertools
# import time
# from threading import Thread
# from googletrans import Translator, constants
#
#
# # class Url_object_main:
# #
# #     def __init__(self, read_file):
# #         with open(read_file) as file:
# #             get_read_file = json.load(file)
# #             # self.read_file = get_read_file["urls"]
# #             self.read_file = get_read_file["urls"][0]["url1"]
# #
# #     try:
# #         def get_date_file_values(self):
# #             return self.read_file
# #     except Exception:
# #         raise f"{WindowsError} Page Was not working"
#
# class URLs_info(Translator):
#
#     def __init__(self, urls):
#         super().__init__()
#         self.urls = urls
#
#     async def get_access(self):
#         """This fucntion extract the title name in the Official Website"""
#         try:
#             if requests.get(self.urls).status_code == 200:
#                 try:
#                     # making requests instance
#                     reqs = requests.get(self.urls)
#                     await asyncio.sleep(1)
#                     return reqs
#                 except Exception as err:
#                     return err
#             else:
#                 print("The given URL is Broken. or URL's shoud be removed or POI has been closed")
#         except Exception as err:
#             return f"Something went wrong in funciotn {id(self.get_access)}{err}"
#
#     async def extract_the_copyrights(self):
#         urls = self.urls
#         webpage = requests.get(urls)
#         soup = BeautifulSoup(webpage.content, 'html.parser')
#         get_name = []
#         for tag in soup.findAll(text=re.compile(r'©|copy;')):
#             copyrighttexts = tag.parent.text
#             get_name.append(copyrighttexts)
#         get_name.append(soup.title.string)
#         await asyncio.sleep(1)
#         return set(get_name[0].strip().split(" "))
#
#     def get_all_urls(self):
#         """GET all the link in the Website"""
#         try:
#             soup = BeautifulSoup(requests.get(self.urls).content, 'html.parser')
#             urls = [link.get('href') for link in soup.find_all('a')]
#             urls_contact = [i for i in set([get_specific_url for get_specific_url in set(urls) \
#                                             if "location" in str(get_specific_url) or "contact" in str(get_specific_url) \
#                                             or "about" in str(get_specific_url) \
#                                             or "facebook" in str(get_specific_url) \
#                                             or "main" in str(get_specific_url)])]
#             if len([i for i in urls_contact if re.compile("^[a-z]|/").findall((str(i)))]) >= 1:
#                 get_d = [None if re.compile(f"http").findall(str(i)) or re.compile(f"/").findall(str(i)) else "/" + i
#                          for i in urls_contact]
#                 # if re.compile(f"http").findall(str(i)):
#                 #     pass
#                 # else:
#                 #     get_d.append(i)
#                 urls_contact2 = [str(self.urls) + "/" + str(i[1::]) for i in itertools.chain(urls_contact, get_d) \
#                                  if str(i).startswith("/")]
#                 get_filter_urls = [i for i in list(map(lambda i: i if str(i).startswith("http") else None,
#                                                        itertools.chain(urls_contact, urls_contact2))) \
#                                    if i is not None]
#                 get_full_filter_url = [self.urls] + get_filter_urls
#                 return get_full_filter_url
#             else:
#                 get_full_filter_url = [self.urls] + urls_contact
#                 return get_full_filter_url
#         except Exception:
#             return f"Invalide URL as been assigned to function [get_the_urls]"
#
#     async def get_all_values(self):
#         try:
#             get_abt_home_main_page, get_all_location_page = [], []
#             for i in self.get_all_urls():
#                 if "about" in i or "contact" in i or "contact-us" in i or "find-us" in i or "find" in i:
#                     get_abt_home_main_page.append(i)
#                 elif "location" in i:
#                     get_all_location_page.append(i)
#                 else:
#                     pass
#             # using the BeautifulSoup module
#             store_url_text_info = []
#             for urlinfo in get_abt_home_main_page:
#                 soup = BeautifulSoup(requests.get(urlinfo).text, 'html.parser')
#                 # displaying the title
#                 # get_txt = [title.strip() for title in soup.text.split()]
#                 for title in soup.text.split():
#                     store_url_text_info.append(title)
#             # await asyncio.sleep(3)
#             return set(store_url_text_info), get_all_location_page
#         except Exception as err:
#             raise f"Values Has been not generated for URL {err}"
#
#     async def get_number(self):
#         """Get the DATA from the URL """
#         try:
#             store_number_info = []
#             # for txt in self.get_all_urls():
#             soup = [BeautifulSoup(requests.get(txt).text, 'html.parser') for txt in self.get_all_urls()]
#             pattern = re.compile(r"\d+")
#             get_num = pattern.findall(str(soup))
#             store_number_info.append(get_num)
#             combine_number_val = set([j for i in store_number_info for j in i])
#             # await asyncio.sleep(2)
#             return combine_number_val
#         except Exception as err:
#             return f"Number Has been not generated for URL {err}"
#
#     async def get_all_text(self):
#         """Will Execute all the text retived from the ULR"""
#         store_number_info = []
#         # for txt in self.get_all_urls():
#         soup = [BeautifulSoup(requests.get(txt).text, 'html.parser') for txt in self.get_all_urls()]
#         pattern = re.compile(r"[A-Z'&a-z0-9]+|@|!|-|'|#|&|%")
#         get_num = pattern.findall(str(soup))
#         store_number_info.append(get_num)
#         # comdine_text_value = set([j for i in store_number_info for j in i])
#         comdine_text_value = [j for i in store_number_info for j in i]
#         # comdine_text_value.union(self.extract_the_copyrights())
#         await asyncio.sleep(0.10)
#         return comdine_text_value
#
#     async def get_phonenumber(self):
#         store_number_info = []
#         for txt in self.get_all_urls():
#             soup = BeautifulSoup(requests.get(txt).content, 'html.parser')
#             pattern = re.compile(r"\(\d{3}\)|\d{3}-\d{4}|\d{3} \d{4}")
#             # pattern2 = re.compile(r"(\+\d{1,2})?[\s.-]?\d{3}[\s.-]?\d{4}")
#             get_num = pattern.findall(str(soup))
#             store_number_info.append(get_num)
#         comdine_phonenumber_value = set([j for i in store_number_info for j in i])
#         # await asyncio.sleep(1)
#         return comdine_phonenumber_value
#
#     async def get_category(self):
#         with open("category.json") as file:
#             get_data = json.load(file)
#             create_df = pd.DataFrame(get_data, columns=['alias', "title"])
#             category_dict = create_df.set_index("alias").to_dict()
#             # category_dict["parents"]
#             is_noun = lambda pos: pos[:2] == 'NN'
#             # do the nlp stuff
#             tokenized = nltk.word_tokenize(str(self.get_all_text()))
#             nouns = [word[1:] for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
#             store_category_parents = []
#             for i in nouns:
#                 try:
#                     store_category_parents.append(category_dict['title'][i])
#                 except KeyError:
#                     pass
#             # await asyncio.sleep(0.50)
#             return f"Missing/Updating Category {store_category_parents}"
#
#
