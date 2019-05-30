# docker images

> Manage Docker images.
> More information: <https://docs.docker.com/engine/reference/commandline/images/>.

- List all Docker images:

`docker images`

- List all Docker images with intermediate included:

`docker images -a`

- List all Docker images numeric IDs:

`docker images -q`

- List all Docker images not used by any container:

`docker images --filter dangling=true`
