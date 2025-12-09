# xdelta

> Delta encoding utility.
> Often used for applying patches to binary files.
> More information: <https://github.com/jmacd/xdelta>.

- Apply a patch:

`xdelta -d -s {{path/to/input_file}} {{path/to/delta_file.xdelta}} {{path/to/output_file}}`

- Create a patch:

`xdelta -e -s {{path/to/old_file}} {{path/to/new_file}} {{path/to/output_file.xdelta}}`
