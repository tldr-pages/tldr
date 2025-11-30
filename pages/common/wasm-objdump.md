# wasm-objdump

> Display information from WebAssembly binaries.
> More information: <https://webassembly.github.io/wabt/doc/wasm-objdump.1.html>.

- Display the section headers of a given binary:

`wasm-objdump {{[-h|--headers]}} {{file.wasm}}`

- Display the entire disassembled output of a given binary:

`wasm-objdump {{[-d|--disassemble]}} {{file.wasm}}`

- Display the details of each section:

`wasm-objdump {{[-x|--details]}} {{file.wasm}}`

- Display the details of a given section:

`wasm-objdump {{[-j|--section]}} '{{import}}' {{[-x|--details]}} {{file.wasm}}`
