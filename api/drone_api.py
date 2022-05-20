from flask_restful import Resource


class DroneApi(Resource):
    route = "/drone/add_image"
    configHeader = "Drone"

    def post(self):
        pass
