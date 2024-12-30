# llvm-config

> 获取编译使用 LLVM 的程序所需的各种配置信息。
> 通常在构建系统中调用，如 Makefile 或配置脚本。
> 更多信息：<https://llvm.org/docs/CommandGuide/llvm-config.html>。

- 编译和链接一个基于 LLVM 的程序：

`clang++ $(llvm-config --cxxflags --ldflags --libs) --output {{path/to/output_executable}} {{path/to/source.cc}}`

- 打印您 LLVM 安装的 `PREFIX`：

`llvm-config --prefix`

- 打印您 LLVM 构建支持的所有目标：

`llvm-config --targets-built`