# docker rmi

> Remove Docker images.
> More information: <https://docs.docker.com/engine/reference/commandline/rmi/>.

- Display help:

`docker rmi`

- Remove one or more images given their names:

`docker rmi {{image1 image2 ...}}`

- Force remove an image:

`docker rmi --force {{image}}`

- Remove an image without deleting untagged parents:

`docker rmi --no-prune {{image}}`
