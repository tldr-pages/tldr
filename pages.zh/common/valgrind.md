# valgrind

> 用于程序剖析、优化和调试的专家工具集的包装器。
> 常用的工具包括 `memcheck`、`cachegrind`、`callgrind`、`massif`、`helgrind` 和 `drd`。
> 更多信息：<https://www.valgrind.org>。

- 使用（默认的）Memcheck 工具显示 `program` 的内存使用情况诊断：

`valgrind {{program}}`

- 使用 Memcheck 报告 `program` 的所有可能内存泄漏的详细信息：

`valgrind --leak-check=full --show-leak-kinds=all {{program}}`

- 使用 Cachegrind 工具剖析并记录 `program` 的 CPU 缓存操作：

`valgrind --tool=cachegrind {{program}}`

- 使用 Massif 工具剖析并记录 `program` 的堆内存和栈使用情况：

`valgrind --tool=massif --stacks=yes {{program}}`