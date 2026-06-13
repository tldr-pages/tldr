# apptainer search

> Search a Container Library for container images.
> More information: <https://apptainer.org/docs/user/main/cli/apptainer_search.html>.

- Search for container images matching a query:

`apptainer search {{query}}`

- Search for container images for a specific architecture:

`apptainer search --arch {{amd64|arm64|386|ppc64le|s390x}} {{query}}`

- Search for only signed container images:

`apptainer search --signed {{query}}`

- Search in a specific Container Library:

`apptainer search --library {{library_url}} {{query}}`

- Display help:

`apptainer search {{[-h|--help]}}`
