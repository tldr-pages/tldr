# unar

> Extract contents from archive files.
> More information: <https://manned.org/unar>.

- Extract an archive to the current directory:

`unar {{path/to/archive}}`

- Extract an archive to the specified directory:

`unar {{[-o|-output-directory]}} {{path/to/directory}} {{path/to/archive}}`

- Force overwrite if files to be unpacked already exist:

`unar {{[-f|-force-overwrite]}} {{path/to/archive}}`

- Force rename if files to be unpacked already exist:

`unar {{[-r|-force-rename]}} {{path/to/archive}}`

- Force skip if files to be unpacked already exist:

`unar {{[-s|-force-skip]}} {{path/to/archive}}`
