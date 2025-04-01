# scontrol

> 查看和修改作业的信息。
> 更多信息：<https://slurm.schedmd.com/scontrol.html>。

- 显示作业的信息：

`scontrol show job {{job_id}}`

- 暂停运行中的作业列表（以逗号分隔）：

`scontrol suspend {{job_id1,job_id2,...}}`

- 恢复暂停的作业列表（以逗号分隔）：

`scontrol resume {{job_id1,job_id2,...}}`

- 挂起排队中的作业列表（使用 `release` 命令允许作业被调度）：

`scontrol hold {{job_id1,job_id2,...}}`

- 释放暂停的作业列表：

`scontrol release {{job_id1,job_id2,...}}`