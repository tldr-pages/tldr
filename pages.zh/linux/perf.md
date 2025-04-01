# perf

> Linux 性能计数器测量框架。
> 更多信息：<https://perf.wiki.kernel.org>。

- 显示命令的基本性能计数器统计信息：

`perf stat {{gcc hello.c}}`

- 显示系统范围的实时性能计数器分析：

`sudo perf top`

- 运行命令并将其分析记录到 `perf.data`：

`sudo perf record {{command}}`

- 记录现有进程的分析到 `perf.data`：

`sudo perf record -p {{pid}}`

- 读取 `perf.data`（由 `perf record` 创建）并显示分析：

`sudo perf report`