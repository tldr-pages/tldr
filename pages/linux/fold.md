# fold

> Folds long lines for fixed-width output devices.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/fold-invocation.html>.

- Fold lines in a fixed width:

`fold {{[-w|--width]}} {{width}} {{path/to/file}}`

- Count width in bytes (the default is to count in columns):

`fold {{[-b|--bytes]}} {{[-w|--width]}} {{width_in_bytes}} {{path/to/file}}`

- Break the line after the rightmost blank within the width limit:

`fold {{[-s|--spaces]}} {{[-w|--width]}} {{width}} {{path/to/file}}`
