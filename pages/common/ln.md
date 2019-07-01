# ln

> Creates links to files and directories.

- Create a symbolic link to a file or directory:

`ln -s {{path/to/file_or_directory}} {{path/to/symlink}}`

- Overwrite an existing symbolic to point to a different file:

`ln -sf {{path/to/new_file}} {{path/to/symlink}}`

- Create a hard link to a file:

`ln {{path/to/file}} {{path/to/hardlink}}`
