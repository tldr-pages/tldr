# dstat

> 用于生成系统资源统计信息的多功能工具。
> 更多信息：<http://dag.wieers.com/home-made/dstat>。

- 显示 CPU、磁盘、网络、分页和系统统计信息：

`dstat`

- 每 5 秒显示一次统计信息，仅更新 4 次：

`dstat {{5}} {{4}}`

- 仅显示 CPU 和内存统计信息：

`dstat --cpu --mem`

- 列出所有可用的 dstat 插件：

`dstat --list`

- 显示使用最多内存和 CPU 的进程：

`dstat --top-mem --top-cpu`

- 显示电池百分比和剩余电池时间：

`dstat --battery --battery-remain`
