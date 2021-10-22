# from .connections_app import register_routes as connection_rest_routes


def register_routes(api, app, root="api"):
    from .controllers import api as connection_api
    api.add_namespace(connection_api, path=f"/{root}")
    # connection_rest_routes(api, app)
