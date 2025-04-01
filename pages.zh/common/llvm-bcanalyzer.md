# llvm-bcanalyzer

> LLVM 位码（`.bc`）分析器。
> 更多信息：<https://llvm.org/docs/CommandGuide/llvm-bcanalyzer.html>.

- 打印位码文件的统计信息：

`llvm-bcanalyzer {{path/to/file.bc}}`

- 打印位码文件的 SGML 表示和统计信息：

`llvm-bcanalyzer -dump {{path/to/file.bc}}`

- 从 `stdin` 读取位码文件并分析：

`cat {{path/to/file.bc}} | llvm-bcanalyzer`