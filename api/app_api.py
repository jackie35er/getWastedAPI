from flask_restful import Resource
from flask import request
from domain.meldung import Meldung
from service.app_service import AppService


class AppApi(Resource):
    route = "/app/add_image"
    configHeader = "App"

    def __init__(self):
        self.service = AppService('https://get-wasted-db-default-rtdb.firebaseio.com/Meldungen.json')

    def post(self):
        if request.is_json:
            data = request.get_json()

            try:
                meldung = Meldung(
                    int(data["user_id"]),
                    data["image"],
                    float(data["longitude"]),
                    float(data["latitude"]),
                    data["timestamp"]
                )
                self.service.add_Meldung(meldung)
                return data, 201
            except KeyError:
                return {"error": "Unknown JSON Format"}, 400
        return {"error": "Request must be JSON"}, 415
