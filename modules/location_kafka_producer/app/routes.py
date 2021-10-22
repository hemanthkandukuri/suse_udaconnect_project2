from .location_service import register_routes as location_service_producer_routes


def register_routes(api, root="api"):
    location_service_producer_routes(api, root=root)
