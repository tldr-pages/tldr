# llvm-dis

> 将LLVM位码文件转换为人类可读的LLVM中间表示（IR）。
> 更多信息：<https://www.llvm.org/docs/CommandGuide/llvm-dis.html>。

- 将位码文件转换为LLVM IR，并将结果写入`stdout`：

`llvm-dis {{path/to/input.bc}} -o -`

- 将位码文件转换为具有相同文件名的LLVM IR文件：

`llvm-dis {{path/to/file.bc}}`

- 将位码文件转换为LLVM IR，并将结果写入指定文件：

`llvm-dis {{path/to/input.bc}} -o {{path/to/output.ll}}`