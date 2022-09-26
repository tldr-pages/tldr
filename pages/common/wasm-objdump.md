# wasm-objdump

> Display information from WebAssembly binaries.
> More information: <https://github.com/WebAssembly/wabt>.

- Display the section headers of a given binary:

`wasm-objdump -h {{file.wasm}}`

- Display the entire disassembled output of a given binary:

`wasm-objdump -d {{file.wasm}}`

- Display the details of each section:

`wasm-objdump --details {{file.wasm}}`

- Display the details of a given section:

`wasm-objdump --section '{{import}}' --details {{file.wasm}}`
