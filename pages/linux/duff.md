# duff

> Duplicate file finder.
> More information: <https://github.com/elmindreda/duff>.

- Find duplicate files recursively:

`duff -r {{path/to/directory}}`

- List all but one file from each cluster of duplicates:

`duff -er {{path/to/directory}}`

- List unique files:

`duff -ur {{path/to/directory}}`

- Use SHA-256 instead of SHA-1:

`duff -d sha256 {{path/to/directory}}`

- Compare files byte by byte instead of using digests:

`duff -t {{path/to/directory}}`

- Include hidden files and directories when searching recursively:

`duff -ar {{path/to/directory}}`
