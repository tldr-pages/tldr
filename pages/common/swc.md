# swc

> JavaScript and TypeScript compiler written in Rust.
> More information: <https://swc.rs>.

- Transpile a specified input file and output to `stdout`:

`swc {{path/to/file}}`

- Transpile the input file every time it is changed:

`swc {{path/to/file}} --watch`

- Transpile a specified input file and output to a specific file:

`swc {{path/to/input_file}} --out-file {{path/to/output_file}}`

- Transpile a specified input directory and output to a specific directory:

`swc {{path/to/input_directory}} --out-dir {{path/to/output_directory}}`

- Transpile a specified input directory using a specific configuration file:

`swc {{path/to/input_directory}} --config-file {{path/to/.swcrc}}`

- Ignore files in a directory specified using glob path:

`swc {{path/to/input_directory}} --ignore {{ignored_files}}`
