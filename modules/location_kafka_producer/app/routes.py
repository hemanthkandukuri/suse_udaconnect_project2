def register_routes(api, root="api"):
    from app.controllers import api as location_kafka_producer
    api.add_namespace(location_kafka_producer, path=f"/{root}")
