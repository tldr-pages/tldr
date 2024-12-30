# wasm2c

> 将文件从 WebAssembly 二进制格式转换为 C 源文件和头文件。
> 更多信息：<https://github.com/WebAssembly/wabt>。

- 将文件转换为 C 源文件和头文件并在控制台显示：

`wasm2c {{file.wasm}}`

- 将输出写入指定文件（`file.h` 也会自动生成）：

`wasm2c {{file.wasm}} -o {{file.c}}`