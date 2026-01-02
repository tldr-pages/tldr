# chown

> Change user and group ownership of files and directories.
> See also: `chgrp`.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/chown-invocation.html>.

- Change the owner user of a file/directory:

`sudo chown {{user}} {{path/to/file_or_directory}}`

- Change the owner user and group of a file/directory:

`sudo chown {{user}}:{{group}} {{path/to/file_or_directory}}`

- Change the owner user and group to both have the name `user`:

`sudo chown {{user}}: {{path/to/file_or_directory}}`

- Change the group of a file to a group that the current user belongs to:

`chown :{{group}} {{path/to/file_or_directory}}`

- Recursively change the owner of a directory and its contents:

`sudo chown {{[-R|--recursive]}} {{user}} {{path/to/directory}}`

- Change the owner of a symbolic link:

`sudo chown {{[-h|--no-dereference]}} {{user}} {{path/to/symlink}}`

- Change the owner of a file/directory to match a reference file:

`sudo chown --reference {{path/to/reference_file}} {{path/to/file_or_directory}}`
