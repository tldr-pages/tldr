# strigger

> 查看或修改 Slurm 触发器信息。
> 触发器是在 Slurm 集群上发生特定事件时自动运行的动作。
> 更多信息：<https://slurm.schedmd.com/strigger.html>.

- 注册新的触发器。当指定事件发生时执行指定的程序：

`strigger --set --{{primary_database_failure|primary_slurmdbd_failure|primary_slurmctld_acct_buffer_full|primary_slurmctld_failure|...}} --program={{路径/到/可执行文件}}`

- 当指定的作业终止时执行指定的程序：

`strigger --set --jobid={{作业ID}} --fini --program="{{路径/到/可执行文件}} {{参数1 参数2 ...}}"`

- 查看活动的触发器：

`strigger --get`

- 查看与指定作业相关的活动触发器：

`strigger --get --jobid={{作业ID}}`

- 清除指定的触发器：

`strigger --clear {{触发器ID}}`
