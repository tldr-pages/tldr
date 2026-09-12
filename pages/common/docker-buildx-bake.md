# docker buildx bake

> Build images from a Bake file using the BuildKit engine.
> More information: <https://docs.docker.com/reference/cli/docker/buildx/bake>.

- Build all targets defined in the default Bake file in the current directory:

`docker buildx bake`

- Build specific targets:

`docker buildx bake {{target1 target2 ...}}`

- Build using a specific Bake file:

`docker buildx bake {{[-f|--file]}} {{path/to/docker-bake.hcl}}`

- Build and load the resulting images into `docker images`:

`docker buildx bake --load`

- Build and push the resulting images to a registry:

`docker buildx bake --push`

- Print the resulting build options without building:

`docker buildx bake --print`

- List the available targets or variables:

`docker buildx bake --list {{targets|variables}}`

- Display help:

`docker buildx bake {{[-h|--help]}}`
