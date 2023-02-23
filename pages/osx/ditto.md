# ditto

> Copy files and directories.
> More information: <https://ss64.com/osx/ditto.html>.

- Overwrite contents of destination directory with contents of source directory:

`ditto {{path/to/source_directory}} {{path/to/destination_directory}}`

- Print a line to the Terminal window for every file that's being copied:

`ditto -V {{path/to/source_directory}} {{path/to/destination_directory}}`

- Copy a given file or directory, while retaining the original file permissions:

`ditto -rsrc {{path/to/source_directory}} {{path/to/destination_directory}}`
