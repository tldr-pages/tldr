# duff

> Duplicate file finder.
> More information: <https://github.com/elmindreda/duff>.

- Find duplicate files in one or more directories:

`duff {{path/to/directory1 path/to/directory2 ...}}`

- Find duplicates, only comparing files of at least a certain size:

`duff {{[-s|--smaller]}} {{size_in_bytes}} {{path/to/directory}}`

- Find duplicates, only considering whole files (not partial):

`duff {{[-w|--whole]}} {{path/to/directory}}`

- Show only the names of duplicate files:

`duff {{[-n|--names]}} {{path/to/directory}}`

- Show hashes of the duplicate files:

`duff {{[-H|--hashes]}} {{path/to/directory}}`
