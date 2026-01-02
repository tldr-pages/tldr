# wasm2wat

> Convert a file from the WebAssembly binary format to the text format.
> More information: <https://webassembly.github.io/wabt/doc/wasm2wat.1.html>.

- Convert a file to the text format and display it to the console:

`wasm2wat {{file.wasm}}`

- Write the output to a given file:

`wasm2wat {{file.wasm}} {{[-o|--output]}} {{file.wat}}`
