# docker images

> Manage Docker images.
> More information: <https://docs.docker.com/engine/reference/commandline/images/>.

- List all docker images:

`docker images`

- List all docker images with intermediate included:

`docker images -a`

- List all docker images numeric IDs:

`docker images -q`

- List all docker images not used by any container:

`docker images --filter dangling=true`
