import asyncio

from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse, abort
from webscaping.url_individual import get_all_text, get_all_urls
import re
# from langdetect import detect
# from googletrans import Translator
# import pandas as pd

app = Flask(__name__)
api = Api(app)


class Varify_name(Resource):

    def post(self):
        try:
            """Payload Section to get the Attributes"""
            parser = reqparse.RequestParser()
            parser.add_argument("url", type=str, required=True, help="This should be a name")
            parser.add_argument("name", action="append", type=str, required=True, help="This should be a name")
            # Getting access to the variable
            data = parser.parse_args()
            url_object = asyncio.run(get_all_text(get_all_urls(data.get("url"))))
            get_result, non_match, get_correct_name, get_incorrect_name = [], [], [], []
            # Name verification word by word
            for i in str(data["name"][0]).split():
                if re.compile(i, flags=0).findall(str(url_object), re.UNICODE):
                    pass
                else:
                    get_result.append(i)
            # Name verification by String
            if re.compile(data["name"][0]).findall(" ".join(url_object)):
                pass
            else:
                non_match.append(data["name"][0])
            # Name checking all name in the list Correct and Incorrect
            if int(len(get_result)) == 0 and int(len(non_match)) == 0:  # Checks the Already Existing correct name
                for i in range(len(data["name"])):
                    if re.compile(data["name"][i]).findall(" ".join(url_object)):
                        get_correct_name.append(data["name"][i])
                    else:
                        get_incorrect_name.append(data["name"][i])
            else:
                for i in range(len(data["name"])):
                    if re.compile(data["name"][i]).findall(" ".join(url_object)):
                        get_correct_name.append(data["name"][i])
                    else:
                        get_incorrect_name.append(data["name"][i])
            return jsonify(dict(Incorrect_val=get_result,
                                top_name_incorrect=non_match,
                                match=get_correct_name,
                                no_match=get_incorrect_name))
        except Exception as e:
            abort(500, message=f"There was an error while processing you request{e}")


#
#
# # class Find_phonenumber(Resource):
# #     def post(self):
# #         """Phone Number Verfication API, Check the Extact Phone number based on the Input Given to the Funtion"""
# #         try:
# #             parser = reqparse.RequestParser()
# #             parser.add_argument("url", type=str, required=True, help="This should be a name")
# #             parser.add_argument("phone_number", type=str, required=True, help="This should be a name")
# #             data = parser.parse_args()
# #             url_object = URLs_info(data.get("url"))
# #             phone_number = data.get("phone_number")
# #             make_pattren = [phone_number[2:5], phone_number[5:8], phone_number[8::]]
# #             get_non_verified_num = [i for i in [None if i in url_object.get_phonenumber() or i in url_object.get_number() \
# #                                         else i for i in make_pattren] if i is not None]
# #             if len(get_non_verified_num) == 0:
# #                 return jsonify(dict(Error="No Error Found"))
# #             else:
# #                 return jsonify(dict(Error=get_non_verified_num))
# #             # store_incorrect_number = []
# #             # if phone_number in url_object.get_number() or url_object.get_phonenumber():
# #             #     pass
# #             # else:
# #             #     store_incorrect_number.append(phone_number)
# #             # if str(list(get_non_verified_num) + store_incorrect_number).split().count("null") == 3:
# #             #     return jsonify(dict(Error="No Error Found"))
# #             # else:
# #             #     return jsonify(dict(Error=(list(get_non_verified_num) + store_incorrect_number)))
# #         except Exception as e:
# #             abort(500, message=f"There was an error while processing you requet{e}")
#
#
# class Get_name(Resource):
#     def get(self):
#         """Get the Validation Check's"""
#         for i in range(len(Data)):
#             return {f"name_{i}": Data}
#
#
# th1 = api.add_resource(Find_phonenumber, "/phone_number")
api.add_resource(Varify_name, "/nameattribute/name")
if __name__ == "__main__":  # this is the main file
    app.run(debug=True)
