import asyncio
from flask import Flask, Blueprint
from flask_restful import Api
from name.api_name import Varify_name
from phonenumber.api_phone_number import Varify_phone_number


async def main():
    app = Flask("Webscaping_API")
    app.config['BUNDLE_ERRORS'] = False
    api_bp = Blueprint('name', __name__)
    api = Api(api_bp)

    app.register_blueprint(api_bp)
    api.add_resource(Varify_name, "/poi-attribute/name", methods=['POST'])
    api.add_resource(Varify_phone_number, "/poi-attribute/phonenumber", methods=['POST'])
    await asyncio.sleep(0.5)
    return app


if __name__ == "__main__":
    asyncio.run(main()).run(debug=True)


