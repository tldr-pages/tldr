# llc

> 将 LLVM 中间表示或位码编译为目标特定的汇编语言。
> 更多信息：<https://www.llvm.org/docs/CommandGuide/llc.html>.

- 将位码或 IR 文件编译为具有相同基本名称的汇编文件：

`llc {{path/to/file.ll}}`

- 启用所有优化：

`llc -O3 {{path/to/input.ll}}`

- 将汇编输出到特定文件：

`llc --output {{path/to/output.s}}`

- 生成完全可重定位、位置独立的代码：

`llc -relocation-model=pic {{path/to/input.ll}}`