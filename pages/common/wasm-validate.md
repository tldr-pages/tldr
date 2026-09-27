# wasm-validate

> Validate a file in the WebAssembly binary format.
> More information: <https://webassembly.github.io/wabt/doc/wasm-validate.1.html>.

- Validate a WebAssembly binary file:

`wasm-validate {{path/to/file.wasm}}`

- Validate a file and show verbose details:

`wasm-validate {{[-v|--verbose]}} {{path/to/file.wasm}}`

- Validate a file, enabling all supported WebAssembly features:

`wasm-validate --enable-all {{path/to/file.wasm}}`

- Validate a file, enabling a specific feature:

`wasm-validate {{--enable-exceptions|--enable-threads|--enable-gc|...}} {{path/to/file.wasm}}`

- Validate a file, disabling a specific feature:

`wasm-validate {{--disable-simd|--disable-multi-value|--disable-tail-call|...}} {{path/to/file.wasm}}`

- Validate a file, ignoring debug names:

`wasm-validate --no-debug-names {{path/to/file.wasm}}`
