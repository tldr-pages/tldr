# apptainer cache list

> List the local Apptainer cache.
> See also: `apptainer cache clean`.
> More information: <https://apptainer.org/docs/user/main/cli/apptainer_cache_list.html>.

- List all cached container images:

`apptainer cache list`

- List cached container images with detailed information:

`apptainer cache list {{[-v|--verbose]}}`

- List only a specific cache type:

`apptainer cache list {{[-T|--type]}} {{library|oci|shub|blob|...}}`

- Display help:

`apptainer cache list {{[-h|--help]}}`
