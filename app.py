from flask import Flask
from flask_restful import Api

from api.app_api import AppApi
from api.drone_api import DroneApi
from setup import setup, Config

if __name__ == '__main__':

    setup()

    app = Flask(__name__)
    api = Api(app)

    apiClasses = [AppApi, DroneApi]

    for apiClass in apiClasses:
        if bool(Config.config('API')[apiClass.configHeader]):
            api.add_resource(apiClass, apiClass.route)
    port = Config.config('RESTFUL')['Port']
    host = Config.config('RESTFUL')['Host']
    app.run(host=host, port=port, debug=True)
