# wasm-interp

> Decode and run a WebAssembly binary file using a stack-based interpreter.
> More information: <https://webassembly.github.io/wabt/doc/wasm-interp.1.html>.

- Parse and type-check a WebAssembly binary file:

`wasm-interp {{path/to/file.wasm}}`

- Run all exported functions in order:

`wasm-interp {{path/to/file.wasm}} --run-all-exports`

- Run a specific exported function:

`wasm-interp {{path/to/file.wasm}} {{[-r|--run-export]}} {{function_name}}`

- Run an exported function with arguments:

`wasm-interp {{path/to/file.wasm}} {{[-r|--run-export]}} {{function_name}} {{[-a|--argument]}} {{i32:42}}`

- Run execution with tracing enabled:

`wasm-interp {{path/to/file.wasm}} --run-all-exports {{[-t|--trace]}}`

- Run a WASI-compliant module:

`wasm-interp {{path/to/file.wasm}} --wasi`
