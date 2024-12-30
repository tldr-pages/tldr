# lli

> 直接执行来自LLVM位码的程序。
> 更多信息：<https://www.llvm.org/docs/CommandGuide/lli.html>。

- 执行一个位码或IR文件：

`lli {{path/to/file.ll}}`

- 带命令行参数执行：

`lli {{path/to/file.ll}} {{argument1 argument2 ...}}`

- 启用所有优化：

`lli -O3 {{path/to/file.ll}}`

- 在链接之前加载动态库：

`lli --dlopen={{path/to/library.dll}} {{path/to/file.ll}}`