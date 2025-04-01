# sbatch

> 向 SLURM 调度器提交批处理作业。
> 更多信息：<https://manned.org/sbatch>.

- 提交批处理作业：

`sbatch {{path/to/job.sh}}`

- 提交批处理作业并指定自定义名称：

`sbatch --job-name={{myjob}} {{path/to/job.sh}}`

- 提交批处理作业并设置 30 分钟的时间限制：

`sbatch --time={{00:30:00}} {{path/to/job.sh}}`

- 提交作业并请求多个节点：

`sbatch --nodes={{3}} {{path/to/job.sh}}`
