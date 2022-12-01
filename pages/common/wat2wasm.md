# wat2wasm

> Convert a file from the WebAssembly text format to the binary format.
> More information: <https://github.com/WebAssembly/wabt>.

- Parse and check a file for errors:

`wat2wasm {{path/to/file.wat}}`

- Write the output binary to a given file:

`wat2wasm {{path/to/file.wat}} -o {{path/to/file.wasm}}`

- Display simplified representation of every byte:

`wat2wasm -v {{path/to/file.wat}}`
