from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse, abort
from webscaping.urls import URLs_info

app = Flask(__name__)
api = Api(app)

Data = []


class Varify_name(Resource):

    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument("url", type=str, required=True, help="This should be a name")
            parser.add_argument("name", type=str, required=True, help="This should be a name")
            data = parser.parse_args()
            url_object = URLs_info(data.get("url"))
            get_name = str(data.get("name")).split()
            get_result = []
            for i in get_name:
                if i in list(url_object.get_all_text()):
                    pass
                else:
                    get_result.append(i)
            if get_result:
                get_data = {"error": get_result}
                Data.append(get_result)
            else:
                get_data = {"error": "No Name Error"}
            Data.append(get_data)
            return jsonify(get_data)
        except Exception as e:
            abort(500, message=f"There was an error while processing you requet{e}")


class Find_phonenumber(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument("url", type=str, required=True, help="This should be a name")
            parser.add_argument("Phone_number", type=str, required=True, help="This should be a name")
            data = parser.parse_args()
            url_object = URLs_info(data.get("url"))
            phone_number = data.get("Phone_number")
            make_pattren = [phone_number[2:5], phone_number[5:8], phone_number[8::]]
            get_non_verified_num = [None if i in url_object.get_phonenumber() or i in url_object.get_number() else i for i in make_pattren]
            return jsonify(get_non_verified_num)
        except Exception as e:
            abort(500, message=f"There was an error while processing you requet{e}")


class Get_name(Resource):
    def get(self):
        for i in range(len(Data)):
            return {f"name_{i}": Data}


api.add_resource(Find_phonenumber, "/phone_number")
api.add_resource(Varify_name, "/nameattribute/name")
api.add_resource(Get_name, "/nameattribute")
if __name__ == "__main__":
    app.run(debug=True)
