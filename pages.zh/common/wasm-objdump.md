# wasm-objdump

> 显示WebAssembly二进制文件的信息。
> 更多信息：<https://github.com/WebAssembly/wabt>。

- 显示给定二进制文件的节标头：

`wasm-objdump -h {{file.wasm}}`

- 显示给定二进制文件的整个反汇编输出：

`wasm-objdump -d {{file.wasm}}`

- 显示每个节的详细信息：

`wasm-objdump --details {{file.wasm}}`

- 显示给定节的详细信息：

`wasm-objdump --section '{{import}}' --details {{file.wasm}}`