# wasm2c

> Convert a file from the WebAssembly binary format to a C source file and header.
> More information: <https://github.com/WebAssembly/wabt>.

- Convert a file to a C source file and header and display it to the console:

`wasm2c {{file.wasm}}`

- Write the output to a given file (`file.h` gets additionally generated):

`wasm2c {{file.wasm}} -o {{file.c}}`
