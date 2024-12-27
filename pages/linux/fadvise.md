# fadvise

> Control linux file caching behavior.
> More information: <https://manned.org/a2disconf.8>.

- Preload a file into cache:

`fadvise {{-a|--advice}} willneed {{path/to/file}}`

- Suggest dropping a file from cache:

`fadvise {{path/to/file}}`

- Display help:

`fadvise --help`
