# docker buildx use

> Set the current builder instance.
> More information: <https://docs.docker.com/reference/cli/docker/buildx/use/>.

- Set a specific builder instance as the current one:

`docker buildx use {{builder_name}}`

- Set a builder as the default for the current context:

`docker buildx use --default {{builder_name}}`

- Set a builder and persist the changes across contexts:

`docker buildx use --global {{builder_name}}`
