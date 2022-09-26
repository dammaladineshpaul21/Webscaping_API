from flask import jsonify
from flask_restful import Resource, reqparse, abort
import numpy as np
from webscaping_file.url_individual import get_all_urls, get_all_text
import re
import asyncio
from name.name_validation_function import error_check, mixed_name, site_varification, check_spacial_case, get_all_val


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


class Varify_name(Payload):

    def __init__(self):
        super().__init__()
        self.url_object = get_all_urls(self.data.get("url"))
        self.error_page = asyncio.run(error_check(self.url_object[0]))
        self.url_object_string = get_all_text(self.url_object)[0]
        self.call_mixed_name = asyncio.run(mixed_name(self.data["name"], self.url_object_string))

    def post(self):
        try:
            get_result, non_match, get_correct_name, get_incorrect_name = [], [], [], []
            error_code = []
            call_error_code = asyncio.run(site_varification(" ".join(self.error_page)))
            if any(call_error_code):
                error_code.append(call_error_code[0])
                return jsonify(get_all_val(get_result, non_match, get_correct_name,
                                           get_incorrect_name, error_code))
            for i in np.array(str(self.data["name"][0]).split()):
                if re.findall(i, str(self.url_object_string)):
                    pass
                else:
                    if re.findall(asyncio.run(check_spacial_case(i, "resources_file/spacial_carecter.json")),
                                  str(self.url_object_string)):
                        pass
                    else:
                        get_result.append(i)

            # Name checking all name in the list Correct and Incorrect
            # Checks the Already Existing correct name
            def check_single_name(single_name):
                return re.findall(self.data["name"][single_name], " ".join(self.url_object_string))

            # Check the individual name of the string
            if int(len(get_result)) == 0:
                for i in range(len(self.data["name"])):
                    # if name match's in the Data extracted from Website append to Correct Name
                    if any(check_single_name(i)):
                        get_correct_name.append(self.data["name"][i])
                    # if name match's in the Data extracted from Website append to Incorrect Name
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
            if len(get_correct_name) == 0 and int(len(self.call_mixed_name)) > 0:
                get_correct_name.append(self.call_mixed_name)
                # return jsonify(get_all_val(get_result, non_match, get_correct_name[0],
                #                            get_incorrect_name, error_code))
            return jsonify(get_all_val(get_result, non_match, get_correct_name,
                                       get_incorrect_name, error_code))
        except Exception as e:
            abort(500, Error_value=f"Unable to process [url and phone_number]/[Broken URL] request or {e}")
