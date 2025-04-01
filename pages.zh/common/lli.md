# lli

> 直接从 LLVM 位码执行程序。
> 更多信息：<https://www.llvm.org/docs/CommandGuide/lli.html>。

- 执行位码或 IR 文件：

`lli {{path/to/file.ll}}`

- 带命令行参数执行：

`lli {{path/to/file.ll}} {{argument1 argument2 ...}}`

- 启用所有优化：

`lli -O3 {{path/to/file.ll}}`

- 在链接前加载动态库：

`lli --dlopen={{path/to/library.dll}} {{path/to/file.ll}}`
