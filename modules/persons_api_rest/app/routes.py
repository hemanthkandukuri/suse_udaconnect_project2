def register_routes(api, app, root="api"):
    from ..app.persons_app import register_routes as attach_person

    # Add routes
    attach_person(api, app)
