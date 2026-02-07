# apptainer cache clean

> Clean the local Apptainer cache.
> See also: `apptainer cache list`.
> More information: <https://apptainer.org/docs/user/main/cli/apptainer_cache_clean.html>.

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

- Display help:

`apptainer cache clean {{[-h|--help]}}`
