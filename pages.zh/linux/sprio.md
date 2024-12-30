# sprio

> 查看决定作业调度优先级的因素。
> 更多信息：<https://slurm.schedmd.com/sprio.html>。

- 查看所有作业调度优先级的决定因素：

`sprio`

- 查看指定作业调度优先级的决定因素：

`sprio --jobs={{job_id_1,job_id_2,...}}`

- 输出更多信息：

`sprio --long`

- 查看指定用户的作业信息：

`sprio --user={{user_name_1,user_name_2,...}}`

- 打印每个决定作业调度优先级因素的权重：

`sprio --weights`