# llvm-config

> 获取编译使用 LLVM 的程序所需的各种配置信息。
> 通常由构建系统调用，如 Makefile 或 configure 脚本。
> 更多信息：<https://llvm.org/docs/CommandGuide/llvm-config.html>。

- 编译并链接基于 LLVM 的程序：

`clang++ $(llvm-config --cxxflags --ldflags --libs) --output {{path/to/output_executable}} {{path/to/source.cc}}`

- 打印 LLVM 安装的 `PREFIX` 路径：

`llvm-config --prefix`

- 打印你的 LLVM 构建支持的所有目标架构：

`llvm-config --targets-built`
