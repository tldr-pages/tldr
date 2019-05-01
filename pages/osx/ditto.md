# ditto

> Copy files and directories.

- Overwrite contents of destination directory with contents of source directory:

`ditto {{path/to/source}} {{path/to/destination}}`

- Print a line to the Terminal window for every file that's being copied:

`ditto -V {{path/to/source}} {{path/to/destination}}`

- Copy a given file or directory, while retaining the original file permissions:

`ditto -rsrc {{path/to/source}} {{path/to/destination}}`
