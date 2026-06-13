# swc

> JavaScript and TypeScript compiler written in Rust.
> More information: <https://swc.rs/docs/usage/cli>.

- Transpile a specified input file and output to `stdout`:

`swc {{path/to/file}}`

- Transpile the input file every time it is changed:

`swc {{path/to/file}} {{[-w|--watch]}}`

- Transpile a specified input file and output to a specific file:

`swc {{path/to/input_file}} {{[-o|--out-file]}} {{path/to/output_file}}`

- Transpile a specified input directory and output to a specific directory:

`swc {{path/to/input_directory}} {{[-d|--out-dir]}} {{path/to/output_directory}}`

- Transpile a specified input directory using a specific configuration file:

`swc {{path/to/input_directory}} --config-file {{path/to/.swcrc}}`

- Ignore files in a directory specified using glob path:

`swc {{path/to/input_directory}} --ignore {{path/to/ignored_file1 path/to/ignored_file2 ...}}`
