kubectl apply -f namespace.yaml
kubectl apply -f application-configmap.yaml
kubectl apply -f db-secret.yaml
kubectl apply -f postgres.yaml
kubectl apply -f udaconnect-connection.yaml
kubectl apply -f udaconnect-frontend.yaml
kubectl apply -f udaconnect-location-consumer.yaml
kubectl apply -f udaconnect-location-producer.yaml
kubectl apply -f udaconnect-persons-grpc.yaml
kubectl apply -f udaconnect-persons-rest.yaml