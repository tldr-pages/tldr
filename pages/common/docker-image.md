# docker image

> Manage Docker images.
> See also `docker build`, `docker import`, and `docker pull`.
> More information: <https://docs.docker.com/engine/reference/commandline/image/>.

- List local Docker images:

`docker image ls`

- Delete unused local Docker images:

`sudo docker image prune`

- Delete all unused images (not just those without a tag):

`sudo docker image prune --all`

- Show the history of a local Docker image:

`sudo docker image history {{image}}`
