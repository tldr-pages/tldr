# sstat

> 查看正在运行的作业信息。
> 更多信息：<https://slurm.schedmd.com/sstat.html>。

- 显示以逗号分隔的作业列表的状态信息：

`sstat --jobs={{job_id}}`

- 显示以逗号分隔的作业列表的作业 ID、平均 CPU 和平均虚拟内存大小，以管道作为列分隔符：

`sstat --parsable --jobs={{job_id}} --format={{JobID,AveCPU,AveVMSize}}`

- 显示可用字段列表：

`sstat --helpformat`