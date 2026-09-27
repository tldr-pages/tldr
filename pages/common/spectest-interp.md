# spectest-interp

> Read a WebAssembly spec test JSON file and run its tests in an interpreter.
> More information: <https://webassembly.github.io/wabt/doc/spectest-interp.1.html>.

- Run spec tests from a JSON file:

`spectest-interp {{path/to/file.json}}`

- Run tests and display verbose output:

`spectest-interp {{[-v|--verbose]}} {{path/to/file.json}}`

- Run tests with a custom value stack size:

`spectest-interp {{[-V|--value-stack-size]}} {{size}} {{path/to/file.json}}`

- Run tests with a custom call stack size:

`spectest-interp {{[-C|--call-stack-size]}} {{size}} {{path/to/file.json}}`

- Run tests, enabling all WebAssembly features:

`spectest-interp --enable-all {{path/to/file.json}}`

- Run tests, enabling a specific feature:

`spectest-interp {{--enable-threads|--enable-gc|--enable-custom-page-sizes|...}} {{path/to/file.json}}`

- Run tests, disabling a specific feature:

`spectest-interp {{--disable-simd|--disable-multi-value|--disable-tail-call|...}} {{path/to/file.json}}`
