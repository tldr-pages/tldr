# sinfo

> 查看 Slurm 节点和分区的信息。
> 请参阅 `squeue` 和 `sbatch`，它们也是 Slurm 工作负载管理器的一部分。
> 更多信息：<https://slurm.schedmd.com/sinfo.html>.

- 显示集群的快速概览：

`sinfo --summarize`

- 查看整个集群中所有分区的详细状态：

`sinfo`

- 查看特定分区的详细状态：

`sinfo --partition {{partition_name}}`

- 查看空闲节点的信息：

`sinfo --states {{idle}}`

- 汇总已死亡节点：

`sinfo --dead`

- 列出已死亡节点及其原因：

`sinfo --list-reasons`