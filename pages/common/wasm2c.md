# wasm2c

> Convert a file from the WebAssembly binary format to a C source file and header.
> More information: <https://webassembly.github.io/wabt/doc/wasm2c.1.html>.

- Convert a file to a C source file and header and display it to the console:

`wasm2c {{file.wasm}}`

- Write the output to a given file (`file.h` gets additionally generated):

`wasm2c {{file.wasm}} {{[-o|--output]}} {{file.c}}`
