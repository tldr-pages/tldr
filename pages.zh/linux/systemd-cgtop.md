# systemd-cgtop

> 显示本地 Linux 控制组层次结构中的前控制组，按其 CPU、内存或磁盘 I/O 负载排序。
> 另请参见：`top`。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/systemd-cgtop.html>。

- 启动交互式视图：

`systemd-cgtop`

- 更改排序顺序：

`systemd-cgtop --order={{cpu|memory|path|tasks|io}}`

- 按时间显示 CPU 使用率而不是百分比：

`systemd-cgtop --cpu=percentage`

- 更改以秒为单位的更新间隔（或以下时间单位之一：`ms`、`us`、`min`）：

`systemd-cgtop --delay={{interval}}`

- 仅计算用户空间进程（不包括内核线程）：

`systemd-cgtop -P`