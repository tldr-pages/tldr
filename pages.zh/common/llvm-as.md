# llvm-as

> LLVM 中间表示（`.ll`）到位码（`.bc`）的汇编器。
> 更多信息：<https://llvm.org/docs/CommandGuide/llvm-as.html>.

- 汇编一个 IR 文件：

`llvm-as -o {{path/to/out.bc}} {{path/to/source.ll}}`

- 汇编一个 IR 文件并在生成的位码文件中包含模块哈希：

`llvm-as --module-hash -o {{path/to/out.bc}} {{path/to/source.ll}}`

- 从 `stdin` 读取一个 IR 文件并汇编它：

`cat {{path/to/source.ll}} | llvm-as -o {{path/to/out.bc}}`
