# poetry cache

> Manage Poetry's cache.
> See also: `asdf`.
> More information: <https://python-poetry.org/docs/cli/#cache>.

- Display Poetry's available caches:

`poetry cache list`

- Remove all packages from a cache (e.g.: PyPI):

`poetry cache clear PyPI --all`

- Remove a specific package from a cache (Note: must be in format `cache:package:version`):

`poetry cache clear {{pypi}}:{{requests}}:{{2.24.0}}`
