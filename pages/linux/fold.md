# Fold

> Folds long lines for fixed-width output devices.
> More information: <https://manned.org/fold>.

- Fold lines in a fixed width:

`fold -w {{width}} {{path/to/file}}`

- Count width in bytes (the default is to count in columns):

`fold -b -w {{width_in_bytes}} {{file_name}}`

- Break the line after the rightmost blank within the width limit:

`fold -s -w {{width}} {{file_name}}`
