# scan-build

> 命令行工具，用于在常规构建过程中对代码库运行静态分析。
> 更多信息：<https://clang-analyzer.llvm.org/scan-build.html>.

- 构建并分析当前目录下的项目：

`scan-build {{make}}`

- 运行命令并将所有后续选项传递给该命令：

`scan-build {{command}} {{command_arguments}}`

- 显示帮助：

`scan-build`