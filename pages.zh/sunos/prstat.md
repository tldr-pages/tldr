# prstat

> 报告活动进程统计信息。
> 更多信息：<https://www.unix.com/man-page/sunos/1m/prstat>.

- 检查所有进程并按 CPU 使用率排序报告统计信息：

`prstat`

- 检查所有进程并按内存使用率排序报告统计信息：

`prstat -s rss`

- 报告每个用户的总使用情况摘要：

`prstat -t`

- 报告进程的微观状态会计信息：

`prstat -m`

- 每秒打印出 CPU 使用率最高的前 5 个进程列表：

`prstat -c -n 5 -s cpu 1`