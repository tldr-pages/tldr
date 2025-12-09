# ptx

> Generate a permuted index of words from text files.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/ptx-invocation.html>.

- Generate a permuted index where the first field of each line is an index reference:

`ptx {{[-r|--references]}} {{path/to/file}}`

- Generate a permuted index with automatically generated index references:

`ptx {{[-A|--auto-reference]}} {{path/to/file}}`

- Generate a permuted index with a fixed width:

`ptx {{[-w|--width]}} {{width_in_columns}} {{path/to/file}}`

- Generate a permuted index with a list of filtered words:

`ptx {{[-o|--only-file]}} {{path/to/filter}} {{path/to/file}}`

- Generate a permuted index with SYSV-style behaviors:

`ptx {{[-G|--traditional]}} {{path/to/file}}`
