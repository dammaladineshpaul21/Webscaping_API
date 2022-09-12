import asyncio
from flask import jsonify
from flask_restful import Resource, reqparse, abort
from webscaping.url_individual import get_all_text, get_all_urls, mixed_name, check_spacial_case, site_varification
import re


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
            get_result, non_match, get_correct_name, get_incorrect_name, error_code = [], [], [], [], []
            call_mixed_name = asyncio.run(mixed_name(data["name"], url_object))
            # Attribute of Error in URL Website
            error_massage = ["HTTP Error 503", "404 forbidden", "404 Not Found", "Error 404 - Page Not Found",
                              "404 Error Pages", "errorCode 1020", "403 Forbidden"]
            # if len(site_varification(" ".join(url_object), error_massage)) is not 0:
            #     error_code.append(site_varification(" ".join(url_object), error_massage))
            #     return jsonify(dict(Incorrect_val=get_result,
            #                         top_name_incorrect=non_match,
            #                         match=get_correct_name,
            #                         no_match=get_incorrect_name,
            #                         error_code=error_code))
            # to check the status of the Mixed Name
            if int(len(call_mixed_name)) > 0 or len(site_varification(" ".join(url_object), error_massage)) is not 0:
                get_correct_name.append(call_mixed_name), \
                error_code.append(site_varification(" ".join(url_object), error_massage))
                return jsonify(dict(Incorrect_val=get_result,
                                    top_name_incorrect=non_match,
                                    match=get_correct_name[0],
                                    no_match=get_incorrect_name,
                                    error_code=error_code[0]))
            # Name verification word by word
            for i in str(data["name"][0]).split():
                if re.compile(i).findall(str(url_object)):
                    pass
                else:
                    if re.compile(asyncio.run(check_spacial_case(i, "resources_file/spacial_carecter.json"))).findall(
                            str(url_object)):
                        pass
                    else:
                        get_result.append(i)
            if len(get_result) > 0:
                # Name verification by String
                if re.compile(data["name"][0]).findall(" ".join(url_object)):
                    pass
                else:
                    if re.compile(asyncio.run(check_spacial_case(data["name"][0], "resources_file/spacial_carecter.json"))).findall(
                            str(url_object)):
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
                                    no_match=get_incorrect_name,
                                    error_code=error_code))
            else:
                get_correct_name.append(data["name"][0])
            return jsonify(dict(Incorrect_val=get_result,   # Final Output
                                top_name_incorrect=non_match,
                                match=get_correct_name,
                                no_match=get_incorrect_name,
                                error_code=error_code))
        except Exception as e:
            abort(500, Error_value=f"Unable to process URL request {e}")
