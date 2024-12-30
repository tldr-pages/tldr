# btrbk

> 创建 btrfs 子卷的快照和远程备份。
> 更多信息：<https://digint.ch/btrbk/doc/readme.html>。

- 打印有关配置的子卷和快照的统计信息：

`sudo btrbk stats`

- 列出配置的子卷和快照：

`sudo btrbk list`

- 打印在不进行实际更改的情况下运行会发生什么：

`sudo btrbk --verbose dryrun`

- 详细运行备份例程，显示进度条：

`sudo btrbk --progress --verbose run`

- 仅为配置的子卷创建快照：

`sudo btrbk snapshot`