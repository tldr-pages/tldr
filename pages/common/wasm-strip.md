# wasm-strip

> Remove sections of a WebAssembly binary file.
> More information: <https://webassembly.github.io/wabt/doc/wasm-strip.1.html>.

- Remove all custom sections from a WebAssembly binary file:

`wasm-strip {{path/to/file.wasm}}`

- Remove sections and write the output to a given file:

`wasm-strip {{[-o|--output]}} {{path/to/output.wasm}} {{path/to/file.wasm}}`

- Keep a specific section in the output (can be specified multiple times):

`wasm-strip {{[-k|--keep-section]}} {{section_name}} {{path/to/file.wasm}}`
