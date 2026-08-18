# docker buildx bake

> Build from a bake definition file.
> More information: <https://docs.docker.com/reference/cli/docker/buildx/bake/>.

- Build using the default bake file:

`docker buildx bake`

- Build specific targets from a bake file:

`docker buildx bake {{[-f|--file]}} {{path/to/docker-bake.hcl}} {{target1 target2 ...}}`

- Print the resulting options for targets without building:

`docker buildx bake {{[-f|--file]}} {{path/to/docker-bake.hcl}} --print {{target}}`

- Build and push images to a registry:

`docker buildx bake --push`

- Build and load images into Docker:

`docker buildx bake --load`

- Override a target configuration from the command line:

`docker buildx bake --set {{*.platform=linux/arm64}}`

- List available targets or variables in the bake configuration:

`docker buildx bake --list={{targets|variables}}`

- Set a bake variable from the command line:

`docker buildx bake --var {{name=value}}`
