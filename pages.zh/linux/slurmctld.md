# slurmctld

> 监控所有其他 Slurm 守护进程和资源，接受工作（作业），并将资源分配给这些作业。
> 更多信息：<https://slurm.schedmd.com/slurmctld.html>。

- 清除上一个检查点中所有先前的 `slurmctld` 状态：

`slurmctld -c`

- 将守护进程的优先级值设置为指定值，通常为负数：

`slurmctld -n {{value}}`

- 将日志消息写入指定文件：

`slurmctld -L {{path/to/output_file}}`

- 显示帮助信息：

`slurmctld -h`

- 显示版本信息：

`slurmctld -V`