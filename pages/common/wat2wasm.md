# wat2wasm

> Convert a file from the WebAssembly text format to the binary format.
> More information: <https://webassembly.github.io/wabt/doc/wat2wasm.1.html>.

- Parse and check a file for errors:

`wat2wasm {{file.wat}}`

- Write the output binary to a given file:

`wat2wasm {{file.wat}} {{[-o|--output]}} {{file.wasm}}`

- Display simplified representation of every byte:

`wat2wasm {{[-v|--verbose]}} {{file.wat}}`
