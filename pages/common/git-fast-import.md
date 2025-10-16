# git fast-import

> Import data into Git repositories using the fast-import stream format.
> More information: <https://git-scm.com/docs/git-fast-import>.

- Import data from a fast-import stream file:

`git fast-import < {{path/to/stream_file}}`

- Import and show statistics:

`git fast-import --stats < {{path/to/stream_file}}`

- Import with a specific maximum number of pack bytes:

`git fast-import --max-pack-size {{size}} < {{path/to/stream_file}}`

- Import and create a new pack file when the current one reaches a certain size:

`git fast-import --big-file-threshold {{size}} < {{path/to/stream_file}}`

- Display help:

`git fast-import --help`
