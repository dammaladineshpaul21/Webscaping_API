# from langdetect import detect
# import pandas as pd
#
# with open("resources_file/language_code.json") as file:
#     read_data = pd.read_json(file)
#     get_df = pd.DataFrame(read_data)
#     get_lag_code = detect("Vlkers")
#
#
# if get_df[get_lag_code].to_dict()["name"]:
#     print(True)
# else:
#     print(False)
import time

# # import pandas as pd
# # import re
# # phone_number = "+17912254492"
# # get_phonecode = phone_number[0:2], phone_number[0:3], phone_number[0:4], phone_number[0:5]
# # # make_pattren = [phone_number[2:5], phone_number[5:8], phone_number[8::]]
# # read_data = pd.read_json("resources_file/phone_number.json")
# # get_Data = pd.DataFrame(read_data, columns=['dial_code'])
# # store_val = []
# # for i in get_phonecode:
# #     if i in get_Data.to_numpy():
# #         store_val.append(str(i))
# #     else:
# #         pass
# # import numpy as np
# #
# # lst = {
# #     "name":{
# #     "(en-us/st)": "Mattresses For Less",
# #     "(en-gb/st)": "Mattresses Less",
# #     "(en-ca/st)": "Mattresses For Less",
# #     "(en/st)": "Mattresses For Less",
# #     "(global/st)": "Mattresses For Less",
# #     "(en-br/st)": "For Less",
# #     "(en-kg/st)": "For Less"
# #   }
# # }
# # get_Sh = np.array(list(lst["name"].items()))
# # get_d = [i[1::] for i in get_Sh]
# # for i in get_d:
# #     print(type(i))
# # import re
# #
# # from webscaping.url_utilites import URLs_info
# # url_object = URLs_info("https://www.cashbackloans.com")
# #
# # data = {
# #     "name": ["Casback Loans", "Cashback Loans Corporate Office", "Cashback Loans", "Dammala Dinesh Paul",
# #              "Atul Kushwaha"]
# # }
# # get_correct_name = []
# # for i in range(len(data["name"])):
# #     if re.compile(data["name"][i]).findall(" ".join(url_object.get_all_text())):
# #         get_correct_name.append(data["name"][i])
# #     else:
# #         pass
# print(get_correct_name)
#     # for i in range(len(data["name"]) - 1):
#     #     for j in str(data["name"][i + 1]).split():
#     #         if j in list(url_object.get_all_text()):
#     #             get_val.append(j)
#     #             if len(get_val) == len(str(data["name"][i + 1]).split()):
#     #                 get_correct_name.append(data["name"][i + 1])
#     #                 # data["name"].remove(get_correct_name[0])
#     #             else:
#     #                 pass
#     #         else:
#     #             pass
#     # data["name"].remove(get_correct_name[0])
#     # print(data["name"])
#
# # if re.compile(get_correct_name[0]).findall(" ".join(url_object.get_all_text())):
# #     print("Yes")
# # else:
# #     print("NO

# error_massage = ["HTTP Error 503", "404 forbidden", "404 Not Found", "Error 404 - Page Not Found",
#                  "404 Error Pages", "errorCode 1020"]
# from functools import reduce
# import timeit
#
# st_time = timeit.timeit()
# def addition(name, name1):
#     return name + " " + name1
#
#
# input_list = ["Munna", "Dammala", "Komal", "Ash", "Mahesh"]
# end_time = timeit.timeit()
# # Without Lambda function
# print(reduce(addition, input_list), end_time-st_time)

# number = ["8974567","8974567", "8974567"]
# print(*(number))


# [i for i in website_number if i not in website_number]
# from flask_restful import fields, marshal
# import json
# resource_fields = {'name': fields.String, 'first_names': fields.List(fields.String)}
# data = {'name': 'Bougnazal', 'first_names' : []}
# print(json.dumps(marshal(data, resource_fields)))