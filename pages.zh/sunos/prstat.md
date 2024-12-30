# prstat

> 报告活动进程统计信息。
> 更多信息：<https://www.unix.com/man-page/sunos/1m/prstat>。

- 检查所有进程并按 CPU 使用情况排序报告统计信息：

`prstat`

- 检查所有进程并按内存使用情况排序报告统计信息：

`prstat -s rss`

- 报告每个用户的总使用摘要：

`prstat -t`

- 报告微状态进程核算信息：

`prstat -m`

- 每秒打印出 CPU 使用前 5 的进程列表：

`prstat -c -n 5 -s cpu 1`