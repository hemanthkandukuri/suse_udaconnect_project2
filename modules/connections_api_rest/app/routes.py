def register_routes(api, app, root="api"):
    from ..app.connections_app import register_routes as attach_connections

    # Add routes
    attach_connections(api, app)
