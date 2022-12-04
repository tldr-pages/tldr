# docker load

> Load Docker images from files or `stdin`.
> More information: <https://docs.docker.com/engine/reference/commandline/load/>.

- Load a Docker image from `stdin`:

`docker load < {{path/to/image_file.tar}}`

- Load a Docker image from a specific file:

`docker load --input {{path/to/image_file.tar}}`

- Load a Docker image from a specific file in quiet mode:

`docker load --quiet --input {{path/to/image_file.tar}}`
