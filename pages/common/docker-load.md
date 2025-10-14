# docker load

> Load Docker images from files or `stdin`.
> More information: <https://docs.docker.com/reference/cli/docker/image/load/>.

- Load a Docker image from `stdin`:

`docker < {{path/to/image_file.tar}} load`

- Load a Docker image from a specific file:

`docker load {{[-i|--input]}} {{path/to/image_file.tar}}`

- Load a Docker image from a specific file in quiet mode:

`docker load {{[-q|--quiet]}} {{[-i|--input]}} {{path/to/image_file.tar}}`
