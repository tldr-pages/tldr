# slurmdbd

> 一个用于 Slurm 的安全企业级数据库接口。
> 更多信息：<https://slurm.schedmd.com/slurmdbd.html>。

- 将守护进程的优先级值设置为指定值，通常为负数：

`slurmdbd -n {{value}}`

- 将 `slurmdbd` 的工作目录更改为 LogFile 路径或 `/var/tmp`：

`slurmdbd -s`

- 显示帮助信息：

`slurmdbd -h`

- 显示版本：

`slurmdbd -V`