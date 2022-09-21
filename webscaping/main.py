from flask import jsonify
from flask_restful import Resource, reqparse, abort
from webscaping.url_individual import *
import re
from phonenumber.main_phonenumber_file import get_number_list, get_ow_number, url_with_number


class Payload(Resource):

    def __init__(self):
        parser = reqparse.RequestParser()
        self.url = parser.add_argument("url", type=str, required=True, help="This should be a Url")
        self.name = parser.add_argument("name", action="append", type=str, required=False, help="This should be a name")
        self.phone_number = parser.add_argument("phone_number", action="append", type=str, required=False,
                                                help="This should be a Phone_number")
        self.data = parser.parse_args()
        self.urlobject2 = self.data.get("url", None)
        self.name_object = self.data.get("name", None)
        self.phone_number_list = self.data.get("phone_number", None)
        self.url_object = loop.run_until_complete(get_all_urls(self.data.get("url")))
        # self.social = asyncio.run(extract_social_mediapage(asyncio.run(get_all_urls(self.data.get("url")))))
        self.url_object_string = asyncio.run(get_all_text(self.url_object))[0]
        self.error_page = asyncio.run(error_check(self.url_object[0]))
        self.call_mixed_name = asyncio.run(mixed_name(self.data["name"], self.url_object_string))


class Varify_name(Payload):

    def post(self):
        try:
            get_result, non_match, get_correct_name, get_incorrect_name = [], [], [], []
            error_code = []
            if int(len(self.call_mixed_name)) > 0:
                get_correct_name.append(self.call_mixed_name)
                return jsonify(get_all_val(get_result, non_match, get_correct_name[0],
                                           get_incorrect_name, error_code))
            call_error_code = asyncio.run(site_varification(" ".join(self.error_page)))
            if any(call_error_code):
                error_code.append(call_error_code[0])
                return jsonify(get_all_val(get_result, non_match, get_correct_name,
                                           get_incorrect_name, error_code))
            for i in str(self.data["name"][0]).split():
                if re.findall(i, str(self.url_object_string)):
                    pass
                else:
                    if re.findall(asyncio.run(check_spacial_case(i, "resources_file/spacial_carecter.json")),
                                  str(self.url_object_string)):
                        pass
                    else:
                        get_result.append(i)

            # # Name checking all name in the list Correct and Incorrect
            # # Checks the Already Existing correct name
            def check_single_name(i):
                return re.findall(self.data["name"][i], " ".join(self.url_object_string))

            if int(len(get_result)) == 0:
                for i in range(len(self.data["name"])):
                    if any(check_single_name(i)):
                        get_correct_name.append(self.data["name"][i])
                    else:
                        get_incorrect_name.append(self.data["name"][i])
            else:
                for i in range(len(self.data["name"])):
                    if any(check_single_name(i)):
                        get_correct_name.append(self.data["name"][i])
                    else:
                        get_incorrect_name.append(self.data["name"][i])
            if len(get_result) > 0:
                # Name verification by String
                if re.findall(self.data["name"][0], " ".join(self.url_object_string)):
                    pass
                else:
                    if re.findall(asyncio.run(
                            check_spacial_case(self.data["name"][0], "resources_file/spacial_carecter.json")),
                            str(" ".join(self.error_page))):
                        pass
                    else:
                        non_match.append(self.data["name"][0])
            return jsonify(get_all_val(get_result, non_match, get_correct_name,
                                       get_incorrect_name, error_code))
        except Exception as e:
            abort(500, Error_value=f"Unable to process [url and phone_number]/[Broken URL] request or {e}")


class Varify_phone_number(Payload):

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
