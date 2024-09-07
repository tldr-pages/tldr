# unar

> Extract contents from archive files.
> More information: <https://manned.org/unar>.

- Extract an archive to the current directory:

`unar {{path/to/archive}}`

- Extract an archive to the specified directory:

`unar -o {{path/to/directory}} {{path/to/archive}}`

- Force overwrite if files to be unpacked already exist:

`unar -f {{path/to/archive}}`

- Force rename if files to be unpacked already exist:

`unar -r {{path/to/archive}}`

- Force skip if files to be unpacked already exist:

`unar -s {{path/to/archive}}`
