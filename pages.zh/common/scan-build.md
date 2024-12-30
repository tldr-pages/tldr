# scan-build

> 命令行工具，用于在代码库上运行静态分析器，作为常规构建的一部分。
> 更多信息：<https://clang-analyzer.llvm.org/scan-build.html>。

- 在当前目录中构建并分析项目：

`scan-build {{make}}`

- 运行一个命令并将所有后续选项传递给它：

`scan-build {{command}} {{command_arguments}}`

- 显示帮助信息：

`scan-build`