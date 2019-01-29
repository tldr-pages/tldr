# chgrp

> Change group ownership of files and folders.

- Change the owner group of a file/folder:

`chgrp {{group}} {{path/to/file}}`

- Recursively change the owner group of a folder and its contents:

`chgrp -R {{group}} {{path/to/folder}}`

- Change the owner group of a symbolic link:

`chgrp -h {{group}} {{path/to/symlink}}`

- Change the owner group of a file/folder to match a reference file:

`chgrp --reference={{path/to/reference_file}} {{path/to/file}}`
