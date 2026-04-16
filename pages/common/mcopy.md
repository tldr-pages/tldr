# mcopy

> Copy MSDOS files to/from Unix.
> Part of the `mtools` package.
> See also: `mdir`, `mdel`, `mmove`.
> Note: Use forward slash (`/`) instead of backlash (`\`) to refer to DOS subdirectories.
> More information: <https://manned.org/mcopy>.

- Copy a file from Linux to an MS-DOS disk or image:

`mcopy {{path/to/source_file}} {{A}}:{{/path/to/target_file}}`

- Copy a file from an MS-DOS disk to the current Linux directory:

`mcopy {{a:file.txt}} .`

- Copy all files from an MS-DOS drive to a Linux directory:

`mcopy {{a:}} {{path/to/directory}}`

- Copy a file to a disk image using the `-i` flag instead of a drive letter:

`mcopy -i {{path/to/image.img}} {{path/to/file}} {{::}}`

- Copy a file from a disk image to the current directory:

`mcopy -i {{path/to/image.img}} {{::file.txt}} .`

- Copy a directory recursively to an MS-DOS disk:

`mcopy -s {{path/to/directory}} {{a:}}`

- Copy a file and preserve attributes:

`mcopy -p {{path/to/file}} {{a:}}`
