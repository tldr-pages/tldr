# wasm-opt

> 优化 WebAssembly 二进制文件。
> 更多信息：<https://github.com/webassembly/binaryen>。

- 应用默认优化并写入指定文件：

`wasm-opt -O {{input.wasm}} -o {{output.wasm}}`

- 应用所有优化并写入指定文件（耗时较长，但生成最优代码）：

`wasm-opt -O4 {{input.wasm}} -o {{output.wasm}}`

- 优化文件以减小文件大小：

`wasm-opt -Oz {{input.wasm}} -o {{output.wasm}}`

- 将二进制文件的文本表示打印到控制台：

`wasm-opt {{input.wasm}} --print`
