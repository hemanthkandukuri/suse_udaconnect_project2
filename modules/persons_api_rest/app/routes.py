from app.models import Person
from app.schemas import PersonSchema


def register_routes(api, app, root="api"):
    from app.controllers import api as persons_api

    api.add_namespace(persons_api, path=f"/{root}")
