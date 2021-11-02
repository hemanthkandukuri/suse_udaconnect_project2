from flask import request, Response
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource

from app.models import Location
from app.schemas import LocationSchema
from app.services import LocationService


DATE_FORMAT = "%Y-%m-%d"

api = Namespace("Location API", description="Loacation API which puts data onto Kafka Producer")  # noqa


@api.route("/locations")
@api.route("/locations/<location_id>")
@api.param("location_id", "Unique ID for a given Location", _in=" ")
class LocationResource(Resource):
    @accepts(schema=LocationSchema)
    def post(self) -> Location:
        request.get_json()
        LocationService.create(request.get_json())
        return Response(status=202)

    @responds(schema=LocationSchema)
    def get(self, location_id) -> Location:
        location: Location = LocationService.retrieve(location_id)
        return location
