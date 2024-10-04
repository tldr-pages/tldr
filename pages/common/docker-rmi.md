# docker rmi

> Remove Docker images.
> More information: <https://docs.docker.com/reference/cli/docker/image/rm/>.

- Display help:

`docker rmi`

- Remove one or more images given their names:

`docker rmi {{image1 image2 ...}}`

- Force remove an image:

`docker rmi --force {{image}}`

- Remove an image without deleting untagged parents:

`docker rmi --no-prune {{image}}`
