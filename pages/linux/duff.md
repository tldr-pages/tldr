# duff

> Find duplicate files.
> See also: `fdupes`, `jdupes`.
> More information: <https://github.com/elmindreda/duff>.

- Find duplicate files in a directory recursively:

`duff -r {{path/to/directory}}`

- Find duplicate files and list all but one file from each cluster:

`duff -er {{path/to/directory}}`

- Find unique files instead of duplicates:

`duff -ur {{path/to/directory}}`

- Search recursively and include hidden files:

`duff -ra {{path/to/directory}}`

- Use a specific message digest function:

`duff -d {{sha256}} -r {{path/to/directory}}`

- Do not report empty files as duplicates:

`duff -zr {{path/to/directory}}`

- Read NUL-terminated paths from `stdin` and print NUL-terminated results:

`find {{path/to/directory}} -type f -print0 | duff -0`
