kubectl apply -f deployment/namespace.yaml
kubectl apply -f deployment/application-configmap.yaml
kubectl apply -f deployment/db-secret.yaml
kubectl apply -f deployment/postgres.yaml
sleep 2m
postgres_pod=$(kubectl get --no-headers=true pods -o custom-columns=":metadata.name" | grep postgres)
sh scripts/run_db_command.sh "${postgres_pod}"
kubectl apply -f deployment/udaconnect-connection.yaml
kubectl apply -f deployment/udaconnect-frontend.yaml
kubectl apply -f deployment/udaconnect-location-consumer.yaml
kubectl apply -f deployment/udaconnect-location-producer.yaml
kubectl apply -f deployment/udaconnect-persons-grpc.yaml
kubectl apply -f deployment/udaconnect-persons-rest.yaml