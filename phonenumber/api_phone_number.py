from name.api_name import Varify_name
from phonenumber.main_phonenumber_file import url_with_number, get_ow_number, get_number_list, get_all_text
from flask import jsonify, abort
import json
import asyncio
import re


class Varify_phone_number(Varify_name):

    def __init__(self):
        super().__init__()
        self.url_with_number = json.loads(url_with_number(self.data.get("url")))
        self.url_object_number = asyncio.run(get_all_text(self.url_object))[1]

    def post(self):
        try:
            phonenumber_list, incorrect_number, correct_number, website_number, result, website_with_number = [], [], \
                                                                                                              [], [], [], []
            # url_with_number = json.loads(self.url_with_number)
            for i in range(len(self.data["phone_number"])):
                if not str(self.data["phone_number"][i]).isidentifier():
                    phonenumber_list.append(asyncio.run(get_number_list(self.data["phone_number"][i])))

            for i in range(len(phonenumber_list)):
                if re.findall(asyncio.run(get_number_list(phonenumber_list[i])),
                              " ".join(self.url_object_number).replace(" ", "")) \
                        and len(phonenumber_list[i]) >= 10:
                    correct_number.append(phonenumber_list[i])
                else:
                    incorrect_number.append(phonenumber_list[i])

            all_OW_number = asyncio.run(get_ow_number(self.data.get("url")))

            if len(all_OW_number) == 0:
                website_number.append("No Phone Number")
                return jsonify(dict(incorrect_number=incorrect_number,
                                    correct_number=correct_number,
                                    website_number={self.data.get("url"): website_number},
                                    url_with_number=self.url_with_number))
            if len(all_OW_number) == 1:
                if all_OW_number[0] not in correct_number:
                    website_number.append(all_OW_number[0])
            else:
                for i in all_OW_number[0]:
                    filternum = asyncio.run(get_number_list(i))
                    if filternum not in correct_number:
                        website_number.append(filternum)
            return jsonify(dict(incorrect_number=incorrect_number,
                                correct_number=correct_number,
                                website_number={self.data.get("url"): website_number},
                                url_with_number=self.url_with_number))

        except Exception as e:
            abort(500, Error_value=f"Unable to process [url and phone_number]/[Broken URL] request or {e}")
