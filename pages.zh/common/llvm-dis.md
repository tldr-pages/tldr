# llvm-dis

> 将 LLVM 位码文件转换为人类可读的 LLVM 中间表示（IR）。
> 更多信息：<https://www.llvm.org/docs/CommandGuide/llvm-dis.html>.

- 将位码文件转换为 LLVM IR 并将结果写入 `stdout`：

`llvm-dis {{path/to/input.bc}} -o -`

- 将位码文件转换为与原文件同名的 LLVM IR 文件：

`llvm-dis {{path/to/file.bc}}`

- 将位码文件转换为 LLVM IR，并将结果写入指定文件：

`llvm-dis {{path/to/input.bc}} -o {{path/to/output.ll}}`