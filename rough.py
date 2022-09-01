# import pandas as pd
# import re
# phone_number = "+17912254492"
# get_phonecode = phone_number[0:2], phone_number[0:3], phone_number[0:4], phone_number[0:5]
# # make_pattren = [phone_number[2:5], phone_number[5:8], phone_number[8::]]
# read_data = pd.read_json("resources_file/phone_number.json")
# get_Data = pd.DataFrame(read_data, columns=['dial_code'])
# store_val = []
# for i in get_phonecode:
#     if i in get_Data.to_numpy():
#         store_val.append(str(i))
#     else:
#         pass
# import numpy as np
#
# lst = {
#     "name":{
#     "(en-us/st)": "Mattresses For Less",
#     "(en-gb/st)": "Mattresses Less",
#     "(en-ca/st)": "Mattresses For Less",
#     "(en/st)": "Mattresses For Less",
#     "(global/st)": "Mattresses For Less",
#     "(en-br/st)": "For Less",
#     "(en-kg/st)": "For Less"
#   }
# }
# get_Sh = np.array(list(lst["name"].items()))
# get_d = [i[1::] for i in get_Sh]
# for i in get_d:
#     print(type(i))
