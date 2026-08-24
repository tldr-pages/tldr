# apptainer cache

> Manage the local Apptainer cache.
> More information: <https://apptainer.org/docs/user/main/cli/apptainer_cache.html>.

- List all cached container images:

`apptainer cache list`

- List cached container images with detailed information:

`apptainer cache list {{[-v|--verbose]}}`

- List only a specific cache type:

`apptainer cache list {{[-T|--type]}} {{library|oci|shub|blob|...}}`

- Clean the entire cache:

`apptainer cache clean`

- Clean only a specific cache type:

`apptainer cache clean {{[-T|--type]}} {{library|oci|shub|blob|...}}`

- Clean cache entries older than a specific number of days:

`apptainer cache clean {{[-D|--days]}} {{days}}`

- Preview what would be cleaned without removing anything:

`apptainer cache clean {{[-n|--dry-run]}}`

- Force clean without confirmation:

`apptainer cache clean {{[-f|--force]}}`
