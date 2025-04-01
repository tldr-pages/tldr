# slurmctld

> 监控所有其他 Slurm 守护进程和资源，接受工作（作业），并为这些作业分配资源。
> 更多信息：<https://slurm.schedmd.com/slurmctld.html>。

- 清除 `slurmctld` 的所有先前状态，从上次检查点开始：

`slurmctld -c`

- 将守护进程的优先级设置为指定值，通常是一个负数：

`slurmctld -n {{value}}`

- 将日志消息写入指定文件：

`slurmctld -L {{path/to/output_file}}`

- 显示帮助信息：

`slurmctld -h`

- 显示版本信息：

`slurmctld -V`
