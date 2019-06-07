# docker images

> Manage Docker images.
> More information: <https://docs.docker.com/engine/reference/commandline/images/>.

- List all Docker images:

`docker images`

- List all Docker images including intermediates:

`docker images -a`

- List the output in quiet mode (only numeric IDs):

`docker images -q`

- List all Docker images not used by any container:

`docker images --filter dangling=true`
