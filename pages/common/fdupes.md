# fdupes

> Finds duplicate files in a given set of directories.
> More information: <https://github.com/adrianlopezroche/fdupes>.

- Search a single directory:

`fdupes {{directory}}`

- Search multiple directories:

`fdupes {{directory1}} {{directory2}}`

- Search a directory recursively:

`fdupes -r {{directory}}`

- Search multiple directories, one recursively:

`fdupes {{directory1}} -R {{directory2}}`

- Search recursively and replace duplicates with hardlinks:

`fdupes -rH {{directory}}`

- Search recursively for duplicates and display interactive prompt to pick which ones to keep, deleting the others:

`fdupes -rd {{directory}}`

- Search recursively and delete duplicates without prompting:

`fdupes -rdN {{directory}}`
