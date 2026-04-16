# mcopy

> Copy MSDOS files to/from Unix.
> Part of the `mtools` package.
> See also: `mdir`, `mdel`, `mmove`.
> Note: Use forward slash (`/`) instead of backlash (`\`) to refer to DOS subdirectories.
> More information: <https://manned.org/mcopy>.

- Copy a file from Linux to an MS-DOS disk or image:

`mcopy {{path/to/source_file}} {{A}}:{{/path/to/target_file}}`

- Copy a file from an MS-DOS disk to the current Linux directory:

`mcopy {{A}}:{{/path/to/source_file}} .`

- Copy all files from an MS-DOS drive to a Linux directory:

`mcopy {{A}}: {{path/to/target_directory}}`

- Copy a file into a DOS disk [i]mage file instead of a drive letter (`::` represents the root directory of the DOS disk):

`mcopy -i {{path/to/image.img}} {{path/to/source_file}} ::/{{path/to/target_file}}`

- Copy a file from a disk image to the current directory:

`mcopy -i {{path/to/image.img}} ::/{{path/to/source_file}} .`

- Copy a directory recur[s]ively to an MS-DOS disk:

`mcopy -s {{path/to/source_directory}} {{A:/path/to/target_directory}}`

- Copy a file and [p]reserve attributes:

`mcopy -p {{path/to/source_file}} {{A:}}`
