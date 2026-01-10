# xdelta

> A delta encoding utility to generate and apply patches to binary files.
> For the modern version (v3), see `xdelta3`.
> More information: <https://manned.org/xdelta>.

- Generate a patch (delta) between two files:

`xdelta delta {{path/to/old_file}} {{path/to/new_file}} {{path/to/patch_file}}`

- Apply a patch to an old file to reconstruct the new file:

`xdelta patch {{path/to/patch_file}} {{path/to/old_file}} {{path/to/new_file}}`

- Generate a patch with a specific compression level:

`xdelta delta -{{0..9}} {{path/to/old_file}} {{path/to/new_file}} {{path/to/patch_file}}`
