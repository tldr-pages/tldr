# docker buildx prune

> Remove the build cache.
> More information: <https://docs.docker.com/reference/cli/docker/buildx/prune/>.

- Remove build cache for currently active builder:

`docker buildx prune`

- Remove cache records based on a specific filter:

`docker buildx prune --filter "{{type=source.local}}"`

- Remove the least recently used cache records until the cache size is below a specific limit:

`docker buildx prune --max-used-space {{128mb}}`

- Delete most recent cache records till specified amount of disk space is available:

`docker buildx prune --reserved-space 2gb`
