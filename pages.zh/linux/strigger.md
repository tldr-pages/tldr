# strigger

> 查看或修改 Slurm 触发器信息。
> 触发器是在 Slurm 集群中发生事件时自动运行的操作。
> 更多信息：<https://slurm.schedmd.com/strigger.html>。

- 注册一个新的触发器。当指定事件发生时执行指定程序：

`strigger --set --{{primary_database_failure|primary_slurmdbd_failure|primary_slurmctld_acct_buffer_full|primary_slurmctld_failure|...}} --program={{path/to/executable}}`

- 当指定作业终止时执行指定程序：

`strigger --set --jobid={{job_id}} --fini --program="{{path/to/executable}} {{argument1 argument2 ...}}"`

- 查看活动触发器：

`strigger --get`

- 查看与指定作业相关的活动触发器：

`strigger --get --jobid={{job_id}}`

- 清除指定的触发器：

`strigger --clear {{trigger_id}}`