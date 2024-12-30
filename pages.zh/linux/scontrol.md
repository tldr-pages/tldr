# scontrol

> 查看并修改作业信息。
> 更多信息： <https://slurm.schedmd.com/scontrol.html>。

- 显示作业信息：

`scontrol show job {{job_id}}`

- 暂停以逗号分隔的正在运行的作业列表：

`scontrol suspend {{job_id1,job_id2,...}}`

- 恢复以逗号分隔的已暂停的作业列表：

`scontrol resume {{job_id1,job_id2,...}}`

- 持有以逗号分隔的排队作业列表（使用 `release` 命令允许作业被调度）：

`scontrol hold {{job_id1,job_id2,...}}`

- 释放以逗号分隔的已暂停作业：

`scontrol release {{job_id1,job_id2,...}}`