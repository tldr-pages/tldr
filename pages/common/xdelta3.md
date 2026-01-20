# xdelta3

> A delta compression tool for binary files.
> More information: <https://github.com/jmacd/xdelta/blob/wiki/CommandLineSyntax.md>.

- Create a patch ([e]ncode) based on a [s]ource file:

`xdelta3 -e -s {{path/to/old_file}} {{path/to/new_file}} {{path/to/patch_file}}`

- Apply a patch ([d]ecompress) to a [s]ource file:

`xdelta3 -d -s {{path/to/old_file}} {{path/to/patch_file}} {{path/to/new_file}}`

- Create a patch with a specific compression level:

`xdelta3 -{{0..9}} -s {{path/to/old_file}} {{path/to/new_file}} {{path/to/patch_file}}`
