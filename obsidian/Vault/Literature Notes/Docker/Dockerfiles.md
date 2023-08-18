#docker/dockerfile
Docker can build images automatically by reading the instructions of a Dockerfile.
A Dockerfile contains all the commands needed to assemble an image.

## passing files to the docker deamon

when building a dockerfile, all files in the same directory as that dockerfile will be sent to the docker deamon which is able to then ADD or COPY relevant files to the final image.

To avoid long building times, it is recommended to add a .dockerignore file to the project. Docker will only send files from the project which are not inside the .dockerignore file.

`for rust it is recommended to add the target folder to the .dockerignore file`

`for node it is recommended to add the node-modules to the .dockerignore file`

## format

The format of a docker file is the following

```dockerfile
# comment
# test comment

INSTRUCTION argument
FROM ubuntu
```

## FROM instruction

sets a base image for subsequent instructions.

a valid `Dockerfile` must start with a `FROM` instruction. The image can be any valid image – it is especially easy to start by **pulling an image** from the [_Public Repositories_](https://docs.docker.com/docker-hub/repos/).

`example` => when running a **rust server** , the base image should include the **rust binary**

From can appear multiple times in a dockerfile to create multiple images or to create a build stage as dependecy for another.

Optionally a name can be given to a build stage by adding `AS name_build` to the `FROM` instruction.
`(FROM ubuntu:22.04 AS pre_stage)`

This assigned optional name can be used in later `FROM` or `COPY --form` instructions to refer to the image build in this stage.



