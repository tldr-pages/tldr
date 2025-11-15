# uv cache

> Manage `uv`'s global cache directory.
> More information: <https://docs.astral.sh/uv/reference/cli/#uv-cache>.

- Show the cache directory path:

`uv cache dir`

- Clean the entire cache (removes all cached packages and environments):

`uv cache clean`

- Clean the cache for specific packages:

`uv cache clean {{package1 package2 ...}}`

- Prune all unreachable objects from the cache:

`uv cache prune`

- Prune cache optimized for CI environments like GitHub Actions:

`uv cache prune --ci`

- Use a specific cache directory:

`uv cache clean --cache-dir {{path/to/cache}}`

- Clean cache with verbose output:

`uv cache clean {{[-v|--verbose]}}`
