# docker image

> Manage Docker images.
> See also: `docker build`, `docker image pull`, `docker image rm`.
> More information: <https://docs.docker.com/reference/cli/docker/image/>.

- List local Docker images:

`docker {{[images|image ls]}}`

- Delete unused local Docker images:

`docker image prune`

- Delete all unused images (not just those without a tag):

`docker image prune {{[-a|--all]}}`

- Show the history of a local Docker image:

`docker {{[history|image history]}} {{image}}`
