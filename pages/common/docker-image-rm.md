# docker image rm

> Remove Docker images.
> More information: <https://docs.docker.com/reference/cli/docker/image/rm/>.

- Remove one or more images given their names:

`docker {{[rmi|image rm]}} {{image1 image2 ...}}`

- Force remove an image:

`docker {{[rmi|image rm]}} {{[-f|--force]}} {{image}}`

- Remove an image without deleting untagged parents:

`docker {{[rmi|image rm]}} --no-prune {{image}}`

- Display help:

`docker {{[rmi|image rm]}}`
