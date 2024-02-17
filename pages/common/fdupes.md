# fdupes

> Finds duplicate files in a set of directories.
> More information: <https://github.com/adrianlopezroche/fdupes>.

- Search a single directory:

`fdupes {{path/to/directory}}`

- Search multiple directories:

`fdupes {{directory1}} {{directory2}}`

- Search a directory recursively:

`fdupes -r {{path/to/directory}}`

- Search multiple directories, one recursively:

`fdupes {{directory1}} -R {{directory2}}`

- Search recursively and replace duplicates with hardlinks:

`fdupes -rH {{path/to/directory}}`

- Search recursively for duplicates and display interactive prompt to pick which ones to keep, deleting the others:

`fdupes -rd {{path/to/directory}}`

- Search recursively and delete duplicates without prompting:

`fdupes -rdN {{path/to/directory}}`
