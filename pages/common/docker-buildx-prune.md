# docker buildx prune

> Removes the build cache.
> More information: <https://docs.docker.com/reference/cli/docker/buildx/prune/>.

- Remove build cache for currently active builder:

`docker buildx prune`

- Filter to delete specific cache records; note multiple filters flags are AND-ed together:

`docker buildx prune --filter "type=source.local"`

- Delete most recent cache records till cache is equal or less than desired size:

`docker buildx prune --max-used-space 128mb`

- Delete most recent cache records till specificed amount of disk space is available:

`docker buildx pruen --reserved-space 2gb`
