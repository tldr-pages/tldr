# docker buildx rm

> Remove one or more builder instances.
> More information: <https://docs.docker.com/reference/cli/docker/buildx/rm/>.

- Remove a builder instance:

`docker buildx rm {{builder_name}}`

- Remove all inactive builders:

`docker buildx rm --all-inactive`

- Remove all inactive builders without prompting for confirmation:

`docker buildx rm --all-inactive --force`
