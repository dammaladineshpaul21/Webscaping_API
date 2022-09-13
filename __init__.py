import asyncio
from flask import Flask, Blueprint
from flask_restful import Api
from webscaping.main import Varify_name


async def main():
    app = Flask(__name__)
    api_bp = Blueprint('webscaping', __name__)
    api = Api(api_bp)

    app.register_blueprint(api_bp)
    api.add_resource(Varify_name, "/nameattribute/name")
    await asyncio.sleep(0.5)
    return app


if __name__ == "__main__":
    asyncio.run(main()).run(debug=True)