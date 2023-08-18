
![[25-07 23#docker_volume && bind]]

![[25-07 23#how to use docker-volume]]

## How to use docker-binds

Alternatively, we can mount a directory from the host system using a bind mount:

```shell
# Create a container that mounts a directory from the host filesystem into the container
docker run  -it --rm --mount type=bind,source="${PWD}"/my-data,destination=/my-data ubuntu:22.04
# Again, there is a similar (but shorter) syntax using -v which accomplishes the same
docker run  -it --rm -v ${PWD}/my-data:/my-data ubuntu:22.04

echo "Hello from the container!" > /my-data/hello.txt

# You should also be able to see the hello.txt file on your host system
cat my-data/hello.txt
exit
```

Bind mounts can be nice if you want easy visibility into the data being stored, but there are a number of reasons outlined at [https://docs.docker.com/storage/volumes/](https://docs.docker.com/storage/volumes/) (including speed if you are running Docker Desktop on windows/mac) for why volumes are preferred.