# sdiag

> 显示 `slurmctld` 执行的信息。
> 更多信息：<https://slurm.schedmd.com/sdiag.html>.

- 显示与 `slurmctld` 执行相关的所有性能计数器：

`sdiag --all`

- 重置与 `slurmctld` 执行相关的性能计数器：

`sdiag --reset`

- 指定输出格式：

`sdiag --all --{{json|yaml}}`

- 指定发送命令的集群：

`sdiag --all --cluster={{cluster_name}}`
