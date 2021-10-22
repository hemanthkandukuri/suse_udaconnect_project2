from .persons_app import register_routes as person_rest_routes


def register_routes(api, app, root="api"):
    person_rest_routes(api, app)
