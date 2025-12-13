# docker image rm

> Remove Docker images.
> More information: <https://docs.docker.com/reference/cli/docker/image/rm/>.

- Remove one or more images given their names:

`docker image rm {{image1 image2 ...}}`

- Force remove an image:

`docker image rm {{[-f|--force]}} {{image}}`

- Remove an image without deleting untagged parents:

`docker image rm --no-prune {{image}}`

- Display help:

`docker image rm`
