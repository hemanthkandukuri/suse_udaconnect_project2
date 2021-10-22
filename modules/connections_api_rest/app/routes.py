from .connections_app import register_routes as connection_rest_routes


def register_routes(api, app, root="api"):
    connection_rest_routes(api, app)
