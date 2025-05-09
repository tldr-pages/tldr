# fadvise

> Control Linux file caching behavior.
> More information: <https://manned.org/fadvise>.

- Preload a file into cache:

`fadvise {{[-a|--advice]}} willneeded {{path/to/file}}`

- Suggest dropping a file from cache:

`fadvise {{path/to/file}}`

- Display help:

`fadvise {{[-h|--help]}}`
