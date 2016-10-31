# unar

> Extract archive file contents.

- Extract archive to current directory:

`unar {{archive}}`

- Extract archive to the specified directory:

`unar -o {{path/to/directory}} {{archive}}`

- Force overwrite when file to be unpacked already exists:

`unar -f {{archive}}`

- Force rename when file to be unpacked already exists:

`unar -r {{archive}}`

- Force skip when file to be unpacked already exists:

`unar -s {{archive}}`
