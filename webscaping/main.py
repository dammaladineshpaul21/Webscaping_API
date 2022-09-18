import asyncio

from flask import jsonify
from flask_restful import Resource, reqparse, abort
from webscaping.url_individual import *
from phonenumber.main_phonenumber_file import get_number_list, phone_number_string, get_ow_number
import re


class Varify_name(Resource):

    @staticmethod
    def post():
        try:
            """Payload Section to get the Attributes"""
            parser = reqparse.RequestParser()
            parser.add_argument("url", type=str, required=True, help="This should be a Url")
            parser.add_argument("name", action="append", type=str, required=True, help="This should be a name")
            # Getting access to the variable
            data = parser.parse_args()
            url_object = asyncio.run(get_all_text(get_all_urls(data.get("url"))))
            url_object2 = asyncio.run(error_check(data.get("url")))
            get_result, non_match, get_correct_name, get_incorrect_name, error_code = [], [], [], [], []
            call_mixed_name = asyncio.run(mixed_name(data["name"], url_object))
            # Attribute of Error in URL Website
            error_massage = ["HTTP Error 503", "404 forbidden", "404 Not Found", "Error 404 - Page Not Found",
                             "Domain for Sale", "Mod_Security"
                                                "404 Error Pages", "errorCode 1020", "403 Forbidden",
                             "Error Page cannot be displayed", "Domain Not Claimed", "This domain is for sale"]
            # to check the status of the Mixed Name
            if len(site_varification(" ".join(url_object2), error_massage)) != 0:
                error_code.append(site_varification(" ".join(url_object), error_massage))
                return jsonify(get_all_val(get_result, non_match, get_correct_name, get_incorrect_name,
                                           error_code[0]))
            if int(len(call_mixed_name)) > 0:
                get_correct_name.append(call_mixed_name)
                return jsonify(get_all_val(get_result, non_match, get_correct_name[0],
                                           get_incorrect_name, error_code))
            # # Name verification word by word
            for i in str(data["name"][0]).split():
                if re.findall(i, str(url_object)):
                    pass
                else:
                    if re.findall(asyncio.run(check_spacial_case(i, "resources_file/spacial_carecter.json")),
                                  str(url_object2)):
                        pass
                    else:
                        get_result.append(i)
            # # Name checking all name in the list Correct and Incorrect
            # # Checks the Already Existing correct name
            if int(len(get_result)) == 0:
                for i in range(len(data["name"])):
                    if re.findall(data["name"][i], " ".join(url_object)):
                        get_correct_name.append(data["name"][i])
                    else:
                        get_incorrect_name.append(data["name"][i])
            else:
                for i in range(len(data["name"])):
                    if re.compile(data["name"][i]).findall(" ".join(url_object)):
                        get_correct_name.append(data["name"][i])

                    else:
                        get_incorrect_name.append(data["name"][i])
            if len(get_result) > 0:
                # Name verification by String
                if re.compile(data["name"][0]).findall(" ".join(url_object)):
                    pass
                else:
                    if re.compile(asyncio.run(check_spacial_case(data["name"][0],
                    "resources_file/spacial_carecter.json"))).findall(str(" ".join(url_object2))):
                        pass
                    else:
                        non_match.append(data["name"][0])
            return jsonify(get_all_val(get_result, non_match, get_correct_name, get_incorrect_name, error_code))
        except Exception as e:
            abort(500, Error_value=f"Unable to process URL request or [Instead Broken URL] and {e}")


class Varify_phone_number(Resource):

    @staticmethod
    def post():
        try:
            """Payload Section to get the Attributes"""
            parser = reqparse.RequestParser()
            parser.add_argument("url", type=str, required=True, help="This should be a Url")
            parser.add_argument("Phone_number", action="append", type=str, required=True,
                                help="This should be a Phone_number")
            data = parser.parse_args()
            # urlobject = asyncio.run(get_all_urls(data.get("url")))
            urlobject2 = asyncio.run(phone_number_string(data.get("url")))
            url_object3 = asyncio.run(error_check(data.get("url")))
            error_massage = ["HTTP Error 503", "404 forbidden", "404 Not Found", "Error 404 - Page Not Found",
                            "Domain for Sale", "Mod_Security"
                                               "404 Error Pages", "errorCode 1020", "403 Forbidden",
                            "Error Page cannot be displayed", "Domain Not Claimed", "This domain is for sale"]

            phonenumber_list, incorrect_number, correct_number, website_number, result,error_code=[], [], [], [], [], []
            if len(site_varification(" ".join(url_object3), error_massage)) != 0:
                error_code.append(site_varification(" ".join(url_object3), error_massage))
                return jsonify(dict(correct_number=correct_number,
                                    incorrect_number=incorrect_number,
                                    website_number=website_number,
                                    error_code=error_code[0]))
            for i in range(len(data["Phone_number"])):
                if not str(data["Phone_number"][i]).isidentifier():
                    phonenumber_list.append(asyncio.run(get_number_list(data["Phone_number"][i])))
            for i in range(len(phonenumber_list)):
                if re.findall(asyncio.run(get_number_list(phonenumber_list[i])), " ".join(urlobject2).replace(" ", "")) \
                        and len(phonenumber_list[i]) >= 10:
                    correct_number.append(phonenumber_list[i])
                else:
                    incorrect_number.append(phonenumber_list[i])
            all_OW_number = list(set(asyncio.run(get_ow_number(data.get("url")))))
            for i in all_OW_number:
                filternum = asyncio.run(get_number_list(i))
                if filternum not in correct_number:
                    website_number.append(filternum)
            return jsonify(dict(correct_number=correct_number,
                                incorrect_number=incorrect_number,
                                website_number=website_number))
        except Exception as e:
            abort(500, Error_value=f"Unable to process [url and phone_number]/[Broken URL] request or {e}")
