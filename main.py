import requests
from flask import Flask, jsonify
from flask_restful import Resource, Api

from webscaping.urls import URLs_info

app = Flask(__name__)
api = Api(app)

Data = []


class Varify_name(Resource):

    def post(self, name: str):
        url_object = URLs_info("https://www.lepaindenosancetres.com")
        get_name = name.split(" ")
        get_result = []
        for i in get_name:
            if i in list(url_object.get_all_text()):
                pass
            else:
                get_result.append(i)
        if get_result:
            get_data = {"name": get_name, "error": f"Incorrect Values {get_result}"}
            Data.append(get_data)
        else:
            get_data = {"name": get_name, "error": "No Name Error"}
        Data.append(get_data)
        return {"name": get_data}


class Get_name(Resource):
    def get(self):
        for i in range(len(Data)):
            return {f"name_{i}": Data}


api.add_resource(Varify_name, "/nameattribute/<string:name>")
api.add_resource(Get_name, "/nameattribute")
if __name__ == "__main__":
    app.run(debug=True)
