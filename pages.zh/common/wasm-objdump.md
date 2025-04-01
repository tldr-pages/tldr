# wasm-objdump

> 显示 WebAssembly 二进制文件中的信息。
> 更多信息：<https://github.com/WebAssembly/wabt>.

- 显示给定二进制文件的节头信息：

`wasm-objdump -h {{file.wasm}}`

- 显示给定二进制文件的完整反汇编输出：

`wasm-objdump -d {{file.wasm}}`

- 显示每个节的详细信息：

`wasm-objdump --details {{file.wasm}}`

- 显示给定节的详细信息：

`wasm-objdump --section '{{import}}' --details {{file.wasm}}`
