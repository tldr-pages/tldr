# valgrind

> 一组专业工具的封装，用于分析、优化和调试程序。
> 常用的工具包括 `memcheck`、`cachegrind`、`callgrind`、`massif`、`helgrind` 和 `drd`。
> 更多信息：<https://www.valgrind.org>。

- 使用（默认）Memcheck 工具显示 `program` 的内存使用诊断：

`valgrind {{program}}`

- 使用 Memcheck 报告 `program` 所有可能的内存泄漏的详细信息：

`valgrind --leak-check=full --show-leak-kinds=all {{program}}`

- 使用 Cachegrind 工具分析和记录 `program` 的 CPU 缓存操作：

`valgrind --tool=cachegrind {{program}}`

- 使用 Massif 工具分析和记录 `program` 的堆内存和栈使用情况：

`valgrind --tool=massif --stacks=yes {{program}}`