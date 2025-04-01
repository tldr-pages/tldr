# sstat

> 查看运行作业的信息。
> 更多信息：<https://slurm.schedmd.com/sstat.html>.

- 显示以逗号分隔的作业列表的状态信息：

`sstat --jobs={{job_id}}`

- 显示以逗号分隔的作业列表的作业ID、平均CPU和平均虚拟内存大小，列之间以竖线分隔：

`sstat --parsable --jobs={{job_id}} --format={{JobID,AveCPU,AveVMSize}}`

- 显示可用的字段列表：

`sstat --helpformat`
