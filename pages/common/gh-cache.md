# gh cache

> Manage GitHub Actions caches.
> More information: <https://cli.github.com/manual/gh_cache>.

- List caches for the current repository:

`gh cache {{[ls|list]}}`

- List caches for a specific repository:

`gh cache {{[ls|list]}} {{[-R|--repo]}} {{owner}}/{{repository}}`

- List caches with a specific cache key prefix:

`gh cache {{[ls|list]}} {{[-k|--key]}} {{key_prefix}}`

- List caches for a specific branch:

`gh cache {{[ls|list]}} {{[-r|--ref]}} refs/heads/{{branch_name}}`

- List caches sorted by least recently accessed:

`gh cache {{[ls|list]}} {{[-S|--sort]}} last_accessed_at {{[-O|--order]}} asc`

- Delete a cache by id:

`gh cache delete {{cache_id}}`

- Delete a cache by key:

`gh cache delete {{cache_key}}`

- Delete all caches:

`gh cache delete {{[-a|--all]}}`
