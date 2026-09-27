# wat-desugar

> Format WebAssembly text format files into a canonical representation.
> More information: <https://webassembly.github.io/wabt/doc/wat-desugar.1.html>.

- Parse and format a `.wat` file and print to `stdout`:

`wat-desugar {{path/to/file.wat}}`

- Parse and format a `.wat` file and write to a specific output file:

`wat-desugar {{path/to/file.wat}} {{[-o|--output]}} {{path/to/output.wat}}`

- Format a file with folded expressions where possible:

`wat-desugar {{path/to/file.wat}} {{[-f|--fold-exprs]}}`

- Generate names for indexed variables:

`wat-desugar {{path/to/file.wat}} --generate-names`

- Format a file, writing all exports inline:

`wat-desugar {{path/to/file.wat}} --inline-exports`

- Format a file, writing all imports inline:

`wat-desugar {{path/to/file.wat}} --inline-imports`

- Format a file, enabling all WebAssembly features:

`wat-desugar {{path/to/file.wat}} --enable-all`
