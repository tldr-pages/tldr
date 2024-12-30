# squeue

> 查看SLURM调度器中排队的作业。
> 更多信息：<https://manned.org/squeue>。

- 查看队列：

`squeue`

- 查看特定用户排队的作业：

`squeue -u {{用户名}}`

- 查看队列并每5秒刷新一次：

`squeue -i {{5}}`

- 查看带有预计开始时间的队列：

`squeue --start`