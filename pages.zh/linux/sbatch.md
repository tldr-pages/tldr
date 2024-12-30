# sbatch

> 将批处理作业提交给 SLURM 调度器。
> 更多信息：<https://manned.org/sbatch>。

- 提交批处理作业：

`sbatch {{path/to/job.sh}}`

- 提交带有自定义名称的批处理作业：

`sbatch --job-name={{myjob}} {{path/to/job.sh}}`

- 提交一个时间限制为 30 分钟的批处理作业：

`sbatch --time={{00:30:00}} {{path/to/job.sh}}`

- 提交一个作业并请求多个节点：

`sbatch --nodes={{3}} {{path/to/job.sh}}`