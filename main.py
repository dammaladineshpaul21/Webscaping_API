from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse, abort
from webscaping.urls import URLs_info
app = Flask(__name__)
api = Api(app)

Data = []


class Varify_name(Resource):

    def post(self):
        try:
            """Payload Section to get the Attributes"""
            parser = reqparse.RequestParser()
            parser.add_argument("url", type=str, required=True, help="This should be a name")
            parser.add_argument("name", action="append", type=str, required=True, help="This should be a name")
            data = parser.parse_args()              # Getting access to the variable"
            if str(data.get("url"))[-1] == "/":
                url_object = URLs_info(str(data.get("url")[0:len(str(data.get("url")))-1]))
            else:
                url_object = URLs_info(data.get("url"))
            get_result = []                            # Check the top name with the official Website
            for i in str(data["name"][0]).split():
                if i in list(url_object.get_all_text()):
                    pass
                else:
                    get_result.append(i)
            if int(len(get_result)) > 0:                # Checks the Already Existing correct name
                get_correct_name = []
                get_val = []
                for i in range(len(data.get("name")) - 1):
                    for j in str(data.get("name")[i + 1]).split():
                        if j in list(url_object.get_all_text()):
                            get_val.append(j)
                            if len(get_val) == len(str(data.get("name")[i + 1]).split()):
                                get_correct_name.append(data.get("name")[i + 1])
                            else:
                                pass
                        else:
                            pass
            #     return jsonify(dict(Error=get_result))
            # else:
            #     # return jsonify(dict(Error="No Name Error"))
                return jsonify(dict(Error=get_result, Correct_Name=get_correct_name))
            else:
                return jsonify(dict(Error="No Error Found"))
        except Exception as e:
            abort(500, message=f"There was an error while processing you request{e}")


class Find_phonenumber(Resource):
    def post(self):
        """Phone Number Verfication API, Check the Extact Phone number based on the Input Given to the Funtion"""
        try:
            parser = reqparse.RequestParser()
            parser.add_argument("url", type=str, required=True, help="This should be a name")
            parser.add_argument("phone_number", type=str, required=True, help="This should be a name")
            data = parser.parse_args()
            url_object = URLs_info(data.get("url"))
            phone_number = data.get("phone_number")
            make_pattren = [phone_number[2:5], phone_number[5:8], phone_number[8::]]
            get_non_verified_num = [i for i in [None if i in url_object.get_phonenumber() or i in url_object.get_number() \
                                        else i for i in make_pattren] if i is not None]
            if len(get_non_verified_num) == 0:
                return jsonify(dict(Error="No Error Found"))
            else:
                return jsonify(dict(Error=get_non_verified_num))
            # store_incorrect_number = []
            # if phone_number in url_object.get_number() or url_object.get_phonenumber():
            #     pass
            # else:
            #     store_incorrect_number.append(phone_number)
            # if str(list(get_non_verified_num) + store_incorrect_number).split().count("null") == 3:
            #     return jsonify(dict(Error="No Error Found"))
            # else:
            #     return jsonify(dict(Error=(list(get_non_verified_num) + store_incorrect_number)))
        except Exception as e:
            abort(500, message=f"There was an error while processing you requet{e}")


class Get_name(Resource):
    def get(self):
        """Get the Validation Check's"""
        for i in range(len(Data)):
            return {f"name_{i}": Data}


api.add_resource(Find_phonenumber, "/phone_number")
api.add_resource(Varify_name, "/nameattribute/name")
api.add_resource(Get_name, "/nameattribute")
if __name__ == "__main__":
    app.run(debug=True)
