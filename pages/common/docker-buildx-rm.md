# docker buildx rm

> Remove one or more builder instances.
> More information: <https://docs.docker.com/reference/cli/docker/buildx/rm/>.

- Remove a docker builder instance:

`docker buildx rm mybuilder`

- Remove all inactive builders:

`docker buildx rm --all-inactive`

- Skip confirmation prompt:

`docker buildx rm --all-inactive --force`
