# docker rmi

> Remove one or more Docker images.
> More information: <https://docs.docker.com/engine/reference/commandline/rmi/>.

- Show help:

`docker rmi`

- Remove one or more space-separated images:

`docker rmi {{image(s)}}`

- Force remove an image:

`docker rmi --force {{image}}`

- Remove an image without delete untagged parents:

`docker rmi --no-prune {{image}}`
