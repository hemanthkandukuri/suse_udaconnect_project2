# UdaConnect
## Folder Structure
Uses the same initial folder structure, 
- `/db/` - has sql files, which are used to seed the postgres DB.
- `/deployment/` - has all the Kubernetes deployment files for all the deployments, services, configs,
- `/docs/` - documentation of the project and few images for cross verification of deployments.
- `/modules/` - has all the service's implementation
- `/scripts/` - has `run_db_command.sh` file used to run the DB scripts. 


## Documentation Files
* `docs/grpc/person.proto` - the proto file used to implement the gRPC server.
* `docs/postman/UdaConnect.postman_collection.json` - has the postman collection along with environment variables json file.
* `docs/postman/UdaConnect.UdaConnect_Environment.postman_environment.json` - has the variables, used in the above file.
* `docs/udaconnect-kubernetes-architecture.png` - architecture diagram.
* `docs/UdaConnect-my-initial-Design.jpeg` - architecture initial scratchpad design diagram.
* `docs/udaconnect-pods.png` - kubernetes pods running in the cluster.
* `docs/udaconnect-services.png` - services configured in the cluster, with the details of exposed port forwarding.
* `docs/kafka-Doc.md` - Kafka installation and verification document.
* `docs/UdaConnect-Architecture-Decision.txt` - Architecture decision summary.
* `docs/UdaConnect-OpenAPI.yaml` - Open API document for all the services. 


## Improvements Done.
* `.github/` folder has the github-actions script, which pushes each service in the modules' folder to dockerhub, 
to its own docker image. 
  * This helps in reducing the build and push process of each image for every frequent change done in the code. 
* `/deployment/deploy.sh` -  a utility shell file to install the entire deployment in a single go. 
This script takes care of seeding the postgres DB as well. 
  * Use the command. `sh deployment/deploy.sh`
* `/deployment/deploy.sh` -  a utility shell file to delete all the deployments, deployed above, in a single go. 
  * Use the command.`sh deployment/delete_all_deployments.sh`
* All the modules are published to my DockerHub account and the deployment files use the Kubernetes CRD to pull those 
images while deployment. 

## URLs
1. Frontend - http://localhost:30000
2. Persons API - http://localhost:30001
3. Connection API - http://localhost:30002
4. Location API - http://localhost:30004

## Docker Builds & Images
Each `module` has its own Dockerfile, this ensuring each module can be deployed into a pod and runs in a container.
This Dockerfile is used by Github-Actions to build and push the respective module's image to DockerHub. 
And the Kubernetes deployment files (CRDs) in `deployment` folder use these images (with a tagged version) to deploy 
and run the pods and expose them via the services defined.

* [connections_api_rest](https://hub.docker.com/repository/docker/hemanthkandukuri/connections_api_rest) hemanthkandukuri/connections_api_rest:v1.0.0
* [frontend](https://hub.docker.com/repository/docker/hemanthkandukuri/frontend) hemanthkandukuri/frontend:v1.0.0
* [location_kafka_consumer](https://hub.docker.com/repository/docker/hemanthkandukuri/location_kafka_consumer) hemanthkandukuri/location_kafka_consumer:v1.0.0
* [location_kafka_producer](https://hub.docker.com/repository/docker/hemanthkandukuri/location_kafka_producer) hemanthkandukuri/location_kafka_producer:v1.0.0
* [persons_api_grpc](https://hub.docker.com/repository/docker/hemanthkandukuri/persons_api_grpc) hemanthkandukuri/persons_api_grpc:v1.0.0
* [persons_api_rest](https://hub.docker.com/repository/docker/hemanthkandukuri/persons_api_rest) hemanthkandukuri/persons_api_rest:v1.0.0