# ptx

> Generate a permuted index of words from one or more text files.
> More information: <https://www.gnu.org/software/coreutils/ptx>.

- Generate a permuted index where the first field of each line is an index reference:

`ptx --references {{path/to/file}}`

- Generate a permuted index with automatically generated index references:

`ptx --auto-reference {{path/to/file}}`

- Generate a permuted index with a fixed width:

`ptx --width={{width_in_columns}} {{path/to/file}}`

- Generate a permuted index with a list of filtered words:

`ptx --only-file={{path/to/filter}} {{path/to/file}}`

- Generate a permuted index with SYSV-style behaviors:

`ptx --traditional {{path/to/file}}`
