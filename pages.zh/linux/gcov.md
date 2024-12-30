# gcov

> 代码覆盖率分析和性能分析工具，用于发现程序中未测试的部分。
> 还显示带有代码段执行频率注释的源代码副本。
> 更多信息：<https://gcc.gnu.org/onlinedocs/gcc/Invoking-Gcov.html>。

- 生成名为 `file.cpp.gcov` 的覆盖报告：

`gcov {{path/to/file.cpp}}`

- 为每个基本块写入单独的执行计数：

`gcov --all-blocks {{path/to/file.cpp}}`

- 将分支频率写入输出文件，并将摘要信息以百分比形式打印到 `stdout`：

`gcov --branch-probabilities {{path/to/file.cpp}}`

- 将分支频率写为采取的分支数量，而不是百分比：

`gcov --branch-counts {{path/to/file.cpp}}`

- 不创建 `gcov` 输出文件：

`gcov --no-output {{path/to/file.cpp}}`

- 写入文件级别以及函数级别的摘要：

`gcov --function-summaries {{path/to/file.cpp}}`