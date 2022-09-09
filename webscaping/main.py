import asyncio

import requests
from flask import jsonify
from flask_restful import Resource, reqparse, abort
from webscaping.url_individual import get_all_text, get_all_urls
import re

# from langdetect import detect
# from googletrans import Translator
# import pandas as pd


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
            abort(500, message=f"There was an error while processing you request{e} fsdaf")





