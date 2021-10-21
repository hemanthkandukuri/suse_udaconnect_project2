from .models import Person  # noqa
from .schemas import PersonSchema  # noqa


def register_routes(api, app, root="api"):
    from .controllers import api as persons_api

    api.add_namespace(persons_api, path=f"/{root}")
