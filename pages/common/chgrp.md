# chgrp

> Change group ownership of files and directories.
> See also: `chown`.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/chgrp-invocation.html>.

- Change the owner group of a file/directory:

`chgrp {{group}} {{path/to/file_or_directory}}`

- Recursively change the owner group of a directory and its contents:

`chgrp {{[-R|--recursive]}} {{group}} {{path/to/directory}}`

- Change the owner group of a symbolic link:

`chgrp {{[-h|--no-dereference]}} {{group}} {{path/to/symlink}}`

- Change the owner group of a file/directory to match a reference file:

`chgrp --reference {{path/to/reference_file}} {{path/to/file_or_directory}}`
