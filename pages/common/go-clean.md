# go clean

> Remove object files and cached files.
> More information: <https://golang.org/cmd/go/#hdr-Remove_object_files_and_cached_files>.

- Print the remove commands only:

`go clean -n`

- Remove build cache:

`go clean -cache`

- Remove cached test results:

`go clean -testcache`

- Remove module cache:

`go clean -modcache`
