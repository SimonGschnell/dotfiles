#programming
#2learn
#docker
#devOps
#virtual_machine
Docker is similar to virtual machines, but docker container share the host os instead of emulating a new os for every application.

The Docker engine operates on a client server principle.
The client is the Docker CLI (command line interface) and the server is the docker daemon that runs in the background.

The client communicates through an API to the docker server and this API operates through 
- Docker images
- Docker Containers 

Docker images are created through dockerfiles which are similar to configuration files. Docker Images contain the dependencies and the compiled code of the application to run.
When you download a image and run it you create a docker container with the application and the dependencies running. You can create multiple containers from one image.

Docker container is a standalone executable software package which includes the application listed in the dockerfile and contain all the dependencies needed to run alone. Containers run in isolation but can communicate with each other if they are added to the same network.

Multiple applications can be stored on one container and the applications on the container can communicate to each other within that container. 

Different docker containers, all run on the same OS (infrastructure)

The containers are completely isolated from the other, which increases security. 

when scaling applications build with docker, kubernetes is used to decide how many container instances should be kept alive to serve the application to users and if a container breaks down, kubernetes handle a restart or shutdowns of the containers.
#kubernetes

![[Persisting storage]]
![[Persisting storage#How to use docker-binds]]


