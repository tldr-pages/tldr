# go clean

> Remove object files and cached files.
> More information: <https://golang.org/cmd/go/#hdr-Remove_object_files_and_cached_files>.

- Print the remove commands instead of actually removing anything:

`go clean -n`

- Delete the build cache:

`go clean -cache`

- Delete all cached test results:

`go clean -testcache`

- Delete the module cache:

`go clean -modcache`
