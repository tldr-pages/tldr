# docker image

> Manage Docker images.
> See also: `docker build`, `docker import`, and `docker pull`.
> More information: <https://docs.docker.com/reference/cli/docker/image/>.

- List local Docker images:

`docker image ls`

- Delete unused local Docker images:

`docker image prune`

- Delete all unused images (not just those without a tag):

`docker image prune {{[-a|--all]}}`

- Show the history of a local Docker image:

`docker image history {{image}}`

- View documentation for `docker image rm`:

`tldr docker rmi`
