# gcov

> 代码覆盖率分析和性能分析工具，用于发现程序中未测试的部分。
> 同时显示注释有代码段执行频率的源代码副本。
> 更多信息：<https://gcc.gnu.org/onlinedocs/gcc/Invoking-Gcov.html>。

- 生成名为 `file.cpp.gcov` 的覆盖率报告：

`gcov {{path/to/file.cpp}}`

- 为每个基本块写入单独的执行次数：

`gcov {{[-a|--all-blocks]}} {{path/to/file.cpp}}`

- 将分支频率写入输出文件，并以百分比形式将摘要信息打印到 `stdout`：

`gcov {{[-b|--branch-probabilities]}} {{path/to/file.cpp}}`

- 以分支被调用的次数而不是百分比形式写入分支频率：

`gcov {{[-c|--branch-counts]}} {{path/to/file.cpp}}`

- 不创建 `gcov` 输出文件：

`gcov {{[-n|--no-output]}} {{path/to/file.cpp}}`

- 写入文件级别的以及函数级别的摘要：

`gcov {{[-f|--function-summaries]}} {{path/to/file.cpp}}`