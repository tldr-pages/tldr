# chown

> Change user and group ownership of files and directories.

- Change the owner user of a file/directory:

`chown {{user}} {{path/to/file_or_directory}}`

- Change the owner user and group of a file/directory:

`chown {{user}}:{{group}} {{path/to/file_or_directory}}`

- Recursively change the owner of a directory and its contents:

`chown -R {{user}} {{path/to/directory}}`

- Change the owner of a symbolic link:

`chown -h {{user}} {{path/to/symlink}}`

- Change the owner of a file/directory to match a reference file:

`chown --reference={{path/to/reference_file}} {{path/to/file_or_directory}}`
