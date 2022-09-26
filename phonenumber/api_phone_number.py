from name.api_name import Varify_name
from phonenumber.main_phonenumber_file import get_ow_number, get_number_list, get_all_text
from flask import jsonify, abort
import asyncio
import re


class Varify_phone_number(Varify_name):

    def __init__(self):
        super().__init__()
        # self.url_with_number = json.loads(url_with_number(self.data.get("url")))
        self.url_object_number = get_all_text(self.url_object)[1]

    def post(self):
        try:
            incorrect_number, correct_number, website_number, result = [], [], [], []

            phonenumber_list = [asyncio.run(get_number_list(self.data["phone_number"][i]))
                                    for i in range(len(self.data["phone_number"]))
                                    if not str(self.data["phone_number"][i]).isidentifier()]

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
                                    website_number=website_number))
            if len(all_OW_number[0]) == 1:
                if asyncio.run(get_number_list(str(all_OW_number[0]))) not in correct_number:
                    website_number.append(all_OW_number[0][0])
            else:
                for i in all_OW_number[0]:
                    filternumber = asyncio.run(get_number_list(i))
                    if filternumber not in correct_number:
                        website_number.append(filternumber)
            return jsonify(dict(incorrect_number=incorrect_number,
                                correct_number=correct_number,
                                website_number=website_number))
        except Exception as e:
            abort(500, Error_value=f"Unable to process [url and phone_number]/[Broken URL] request or {e}")
