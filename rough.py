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

import re

get_correct_name = []
data = dict(name=["Carolina Herrera"])
string = "OCTYPE html html lang en - US head title Just a moment title meta content text html charset utf - 8 http - equiv Content - Type meta content IE Edge http - equiv X - UA - Compatible meta content noindex nofollow name robots meta content width device - width initial - scale 1 name viewport link href cdn - cgi styles challenges css rel stylesheet head body class no - js div class main - wrapper role main div class main - content h1 class zone - name - title h1 img class heading - favicon onerror this onerror null this parentNode removeChild this src favicon ico www carlinaherrera com h1 h2 class h2 id challenge - running Checking if the site connection is secure h2 noscript div id challenge - error - title div class h2 span class icon - wrapper div class heading - icon warning - icon div span span id challenge - error - text Enable JavaScript and cookies to continue span div div noscript div id trk jschal js style display none background - image url ' cdn - cgi images trace managed nojs transparent gif ray 747f58fc9fe24ae1' div div class core - msg spacer id challenge - body - text www carolinaherrera com needs to review the security of your connection before proceeding div form action cf chl f tk lUe2Xw945poemxUeXXH3DjPpusmJ6WAuBuzAj0I06MA - 1662720465 - 0 - gaNycGzNB2U enctype application x - www - form - urlencoded id challenge - form method POST input name md type hidden value l57 p4PeXcbK5CkBCqUjS1TnbeAz9D9mtsV5TUb GCk - 1662720465 - 0 - AVJM8QbrBmmQ1NmVyfJ1D8I6zkPCoOKSBZvllKe6uXFuKed8bWpg6fln6McBWXR8fU2SuLRb7v - 8VBrbLTInq4haxxnbU o3D1rrE - mfFwdnBeFdsu3YaPITPPo7W8AjkTHYcGJ65k 9MoXdh lK5FQVWBgFaNk6m9udRT6Lh - nTLEEjsYaBl5Q4yLzI5b5xcbFjmUn3Bk0fmO - HvKxTSdbIJPG43Vp 1yGDVf6tzwpSqVlNv94TPMmwO lZsbe8owaQMS3KdtinOaFu7EQu7FmWXO8beqcMeloKwZJqDtwjXFMlWnyLSDHFAfSOEma83ikTlgudUq4HkDyQ - q9hqSJIVzYj6Lh2KabWTE5RWpv1U9riF xJ0aQCJ8Rq - uyDWKLnHwCQAiSPYn Imi0KtbaKBz4BodR0NmNMPQlp3SnFJ2h5GCQFJ5DSz5JAMHFdWnN rpTtbigAMDRMblei2WiWvgBVgWqWuUt4iLJdRLREs2iuGHrG - Fr98NnWDDO4QXq XXgk7Q4no4c5PteItr - lO3FjHBYUoeR2y C7BSCHajYiU6DMx1u1ahjT79jU7aJW17oVuLnZ2 lUksgqH1uKoyEaGIEzDiFGe95wUQ5C8AgOW - kdmOlQu0mBuW2bbFxlUIIkmOsHthgiFqoo51A input name r type hidden value bdAYnMW7iizdj8k22Mv6iK3Dftz0XZ8 Z9fJ9ecQbHw - 1662720465 - 0 - AcS eRwPaDs00IEtklUlHF2bq7iy91b4imBeZHozlzZX WRXv7O2RxuxRZdp66562bS2 GTnJ3YynkiBMYmQKgfod53hyCcMcgHa9dx6MGX1mIMyIi4sS6jreNVSWmZdT q9hoqbUaq2Re47jR23AwfC5n4UvsSRWCPXRGaJ83636LpwUDSU83sC2H3KzIYGd1Lxo0Z6LrmCmBe2n tU8 54FLfYrFVqMlidy8qKBIh6ZT9DCqlzFwyTUjCBqVKJx dVqorAQHzCmBy cHxMUHaJl JMaj6H7 xy64qqYvbzsWi6Ivin56UXFUJsQHtqtxKwSJG3 QBhnLROFNxK9HStOD25 sgVscfHj9tvJ9RYryGS967E9 v5lVOFF BFXs XOT62W9fg CNgUfWN9FDbNaDt7Sf3DGVI2apKcW9edWAETjCy5I9kto0Vvl yVmGd4YjcadfSp0N4INHf2QrtcAGco EWCeu0Nh60 G qSZQUBFxcrKlWZC5YMe9CE3efMalkFoLVH5YvlOIr8K8aKTHFc8ScgcRdi25LchOFJGHeI39C iYNxSqNIvHTGGdjJwaKvlmuI9VMM6 Q4b YuBKcxlSNVviudxgrEph1dQ0cx2L56DGw3bO4WXyWBmMLZQTO 1jKmrgzY43384hkMim2Zg3cOp VMBdkg9FiyM38pRpGelSob8EbZFVs2Iigo3vcnIOiC9UVMw0qJHRrwKHHTa9kxnyymzE 5W4EijUj4 x QpBVGnqRYvpv5mXBCg21rBj1F S5GHk7ojaV5V2D8Ia2tzFuhrhA6b vpY ng Thn8 QUmUsjWJpN6z2cE7y33V10NFwLBBgy2K JalMw8NGcAEt2CmCwgqD1fCNyqLJwyt6TKUiZEeGTeP81SKphrGtXMMt5APPkM dlDAPjgxBKqash6hHI2tT1QpaL6TUXc esz0FhsPfkEtVWRzqTGByYyxbdkzYvUlLitTATfKC7mU Db uTHevcndAId Ff4HrxhxDtb93DolcMQb61CmnPEPL0DWO9di WvyvGWQ0Jxfsx vtLNXrYw4kGtEvZqF4wlWRYxtApkM0w88xYZKvMAmn2fiQLmzkHPKthE2iAb 7AiYIGPAgxDRDb83GLhV1x Xaioe7R8u2ZNtQ5W6ozLynR BfUJtov2S6FJ1D AYykY flSDtBGYM1THdapopxU5RH6Pa2kdBgCpFdud7EEfaaQgSZF FtEUVAyy9lhNuPn j3nVPIFEWV0TTbIvHhuHR A7HeZdBq IklBHwEZyN3l xyJTZffnekqXEkVtEEcetnjOwmbMjiKEpuLB uuQHeoOHRENSUs5BbHJeCFuQ6ZrXynD KrGJUgE1AV5m9BC4ajgigkbTzfMC6rHDZu cA8A0wC ivbLrpMqr2nbT8GCXqQ6f3cnVUsU2SpGda9 iMBme603Jp9z4X5CEK6jWDPOH rU4 DPq q PE9vQYG2jWdTz3uCCuKvRLHu6eqKl6A bs5wOFrCWz8 lS1qIJQLeYZ IRCfMHDloO6Qcv2vqwPDtWgQ39DsVb2YcqZkW 2AJdJrL0ga68tp oFMZ Pw98q1kvhl AxeFXMPBKiKu72yRqFu4sGNdHvmrCozwx4IBdT795l bMsuDneHzDZFwdt7VIr34pYGZgQGIrt F P0 h6z Qi kJK 7zDH9Qzfb6n0pBKMCQfagDORGq9AZSmW4Syv6ZbvScPvP4JxBNue5AwMuJrylJY 7DeYWjSMqB7XkAW3F4bRVQYktRJhR21UdFr TOy o1dC ryNvVwe zSBjeSckzzzs2S4A08F6 form div div script function window cf chl opt cvId '2' cType 'managed' cNounce '55492' cRay '747f58fc9fe24ae1' cHash '93b678e890358e5' cUPMDTk cf chl tk lUe2Xw945poemxUeXXH3DjPpusmJ6WAuBuzAj0I06MA - 1662720465 - 0 - gaNycGzNB2U cFPWv 'g' cTTimeMs '1000' cTplV 4 cTplB 'cf' cRq ru 'aHR0cHM6Ly93d3cuY2Fyb2xpbmFoZXJyZXJhLmNvbS8 ' ra 'cHl0aG9uLXJlcXVlc3RzLzIuMjguMQ ' rm 'R0VU' d 'xJpwaH6deSqDpjFfITunlIFp ikhgGPptXwfLK7Tth2umd3qxCI4BH gtQaeL6qqW 7hHQYQNT9 wfU4IKflNzbN7YmsowGtivhezftMXRYhYo58IPsAznIysFRIpaZAZf7pebt1nT7neP4yCgJ5 rEmEqY89Vi pWeQwsdAlja5ZaDvLm HVedUno4HmPtTuJlNc99ejRJn 0F3ZaGve rLrBMK0Im8HDBLqlIDJTUrybS5QjLJD65uLM21Y0i bCvht98ZbFHUCqeWNvS1WY1AoslNxW 5bCWMbRsLRZDQ7YjBtB0yn1zTmupXdg2H3tKwWlF5kZvJ84JP0g8lDIq5FXoYg zs71mC j u nBAZNCCRf4K4XDkEjwg3UaPMPFpiDCVi5RXiYzy69digldrhjCDq qHqQ YuSg89aDrLA 3HWaq vMEICyopePfSAaWqZFF3HakKaGHo5fVW36WKbJ4nr3reulZHEOHGAHN6Ww4 5QqyBuFQQ0xMJQxP8TK3X9qGwQeT7Cdexwn9GSzvTYazNV8hpimK3DCTexl QZLIoIy1I5Rl2vNx7wndinyWJPSVDWocsezh nc1Atr4D6rKexZTJMDbMitIodKA9UqEgEh978c AqLQh6MBy3UqTg0mQdUERQd JWPJA ' t 'MTY2MjcyMDQ2NS40MDcwMDA ' m 'FyVa3FVzp2NchYax1ZCBFwdEL4zx8jp4h jqidZJlU0 ' i1 'hC bx1mKdt4sFDh0 o4HUw ' i2 'TY c7uoqwwP7uM2TfLG84Q ' zh 'gTOx78 AY7PZvcImkMS8oWFEVFCjseWbCO9Hi0YdEUE ' uh 'SLdVolODg SO356HusO5I hbfOpiiOxQXj62i MUkA ' hh 'CIi9CDlKTlccOqKwViPD73PoGc3qzLatGe2O7gxn7nI ' var trkjs document createElement 'img' trkjs setAttribute 'src' ' cdn - cgi images trace managed js transparent gif ray 747f58fc9fe24ae1' trkjs setAttribute 'style' 'display none' document body appendChild trkjs var cpo document createElement 'script' cpo src ' cdn - cgi challenge - platform h g orchestrate managed v1 ray 747f58fc9fe24ae1' window cf chl opt cOgUHash location hash '' && location href indexOf ' # ' ! - 1 ' # ' location hash window cf chl opt cOgUQuery location search '' && location href slice 0 - window cf chl opt cOgUHash length indexOf ' ' ! - 1 ' ' location search if window history && window history replaceState var ogU location pathname window cf chl opt cOgUQuery window cf chl opt cOgUHash history replaceState null null cf chl rt tk lUe2Xw945poemxUeXXH3DjPpusmJ6WAuBuzAj0I06MA - 1662720465 - 0 - gaNycGzNB2U window cf chl opt cOgUHash cpo onload function history replaceState null null ogU document getElementsByTagName 'head' 0 appendChild cpo script div class footer role contentinfo div class footer - inner div class clearfix diagnostic - wrapper div class ray - id Ray ID code 747f58fc9fe24ae1 code div div div class text - center Performance &amp security by a href https www cloudflare com utm source challenge&amp utm campaign m rel noopener noreferrer target blank Cloudflare a div div div body html"
if len(get_correct_name) == 0:
    if re.compile(data["name"][0].replace(" ", "").lower()).findall(string):
        print("yes")
    else:
        print("No")
