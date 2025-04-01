# squeue

> 查看 SLURM 调度器中的排队作业。
> 更多信息：<https://manned.org/squeue>.

- 查看排队情况：

`squeue`

- 查看特定用户的排队作业：

`squeue -u {{username}}`

- 每隔 5 秒刷新排队情况：

`squeue -i {{5}}`

- 查看排队情况及预期开始时间：

`squeue --start`
