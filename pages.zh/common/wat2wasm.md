# wat2wasm

> 将 WebAssembly 文本格式文件转换为二进制格式。
> 更多信息：<https://github.com/WebAssembly/wabt>。

- 解析并检查文件错误：

`wat2wasm {{file.wat}}`

- 将输出的二进制文件写入指定文件：

`wat2wasm {{file.wat}} -o {{file.wasm}}`

- 显示每个字节的简化表示：

`wat2wasm -v {{file.wat}}`
