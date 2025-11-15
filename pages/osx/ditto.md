# ditto

> Copy files and directories.
> More information: <https://keith.github.io/xcode-man-pages/ditto.1.html>.

- Overwrite contents of destination directory with contents of source directory:

`ditto {{path/to/source_directory}} {{path/to/destination_directory}}`

- Print a line to the Terminal window for every file that's being copied:

`ditto -V {{path/to/source_directory}} {{path/to/destination_directory}}`

- Copy a given file or directory, while retaining the original file permissions:

`ditto -rsrc {{path/to/source_directory}} {{path/to/destination_directory}}`
