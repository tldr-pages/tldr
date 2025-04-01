# wasm2c

> 将 WebAssembly 二进制格式文件转换为 C 源文件和头文件。
> 更多信息：<https://github.com/WebAssembly/wabt>。

- 将文件转换为 C 源文件和头文件，并将其输出到控制台：

`wasm2c {{file.wasm}}`

- 将输出写入指定文件（同时生成 `file.h`）：

`wasm2c {{file.wasm}} -o {{file.c}}`
