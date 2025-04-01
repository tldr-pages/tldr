# sprio

> 查看决定作业调度优先级的因素。
> 更多信息：<https://slurm.schedmd.com/sprio.html>.

- 查看决定所有作业调度优先级的因素：

`sprio`

- 查看指定作业的调度优先级：

`sprio --jobs={{job_id_1,job_id_2,...}}`

- 输出更多详细信息：

`sprio --long`

- 查看指定用户的作业信息：

`sprio --user={{user_name_1,user_name_2,...}}`

- 输出决定作业调度优先级的各因素的权重：

`sprio --weights`