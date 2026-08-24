# duff

> Command-line utility for identifying duplicate files in a set of directories.
> More information: <https://github.com/elbohs/duff>.

- Search specified directories for duplicate files:

`duff {{path/to/directory1 path/to/directory2 ...}}`

- Search directories recursively:

`duff -r {{path/to/directory}}`

- Search for duplicates while ignoring empty files:

`duff -e {{path/to/directory}}`

- Excessively quiet mode (suppress header information):

`duff -q {{path/to/directory}}`