# opt

> 执行优化和分析 LLVM 源文件。
> 更多信息：<https://llvm.org/docs/CommandGuide/opt.html>.

- 在位码文件上运行优化或分析：

`opt -{{passname}} {{path/to/file.bc}} -S -o {{file_opt.bc}}`

- 将函数的控制流图输出到 `.dot` 文件：

`opt {{-dot-cfg}} -S {{path/to/file.bc}} -disable-output`

- 在级别 2 进行程序优化，并将结果输出到另一个文件：

`opt -O2 {{path/to/file.bc}} -S -o {{path/to/output_file.bc}}`