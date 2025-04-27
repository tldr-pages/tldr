# fdupes

> Finds duplicate files in a set of directories.
> More information: <https://github.com/adrianlopezroche/fdupes>.

- Search a single directory:

`fdupes {{path/to/directory}}`

- Search multiple directories:

`fdupes {{directory1}} {{directory2}}`

- Search a directory recursively:

`fdupes {{[-r|--recurse]}} {{path/to/directory}}`

- Search multiple directories, one recursively:

`fdupes {{path/to/irectory1}} {{[-R|--recurse:]}} {{path/to/directory2}}`

- Search recursively, considering hardlinks as duplicates:

`fdupes {{[-rH|--recurse --hardlinks]}} {{path/to/directory}}`

- Search recursively for duplicates and display interactive prompt to pick which ones to keep, deleting the others:

`fdupes {{[-rd|--recurse --delete]}} {{path/to/directory}}`

- Search recursively and delete duplicates without prompting:

`fdupes {{[-rdN|--recurse --delete --noprompt]}} {{path/to/directory}}`
