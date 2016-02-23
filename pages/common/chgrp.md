# chgrp

> Change group ownership of files and folders.

- Change the owner of a file/folder:

`chgrp {{group}} {{path/to/file}}`

- Recursively change the owner of a folder and its contents:

`chgrp -R {{group}} {{path/to/folder}}`

- Change the owner of a symbolic link:

`chgrp -h {{user}} {{path/to/symlink}}`

- Change the owner of a file/folder to match a reference file:

`chgrp --reference={{path/to/reference_file}} {{path/to/file}}`
