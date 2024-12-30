# llc

> 将LLVM中间表示或位码编译为特定于目标的汇编语言。
> 更多信息请访问：<https://www.llvm.org/docs/CommandGuide/llc.html>。

- 将位码或IR文件编译为具有相同基础名称的汇编文件：

`llc {{path/to/file.ll}}`

- 启用所有优化：

`llc -O3 {{path/to/input.ll}}`

- 将汇编输出到特定文件：

`llc --output {{path/to/output.s}}`

- 输出完全可重定位的、位置独立的代码：

`llc -relocation-model=pic {{path/to/input.ll}}`