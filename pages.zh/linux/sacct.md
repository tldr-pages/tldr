# sacct

> 显示来自 Slurm 服务的会计数据。
> 更多信息：<https://slurm.schedmd.com/sacct.html>.

- 显示最近作业的作业 ID、作业名称、分区、账户、分配的 CPU 数量、作业状态和作业退出代码：

`sacct`

- 显示最近作业的作业 ID、作业状态和作业退出代码：

`sacct --brief`

- 显示一个作业的分配情况：

`sacct --jobs {{job_id}} --allocations`

- 显示一个作业的运行时间、作业名称、请求的 CPU 数量和请求的内存：

`sacct --jobs {{job_id}} --format=Elapsed,JobName,ReqCPUS,ReqMem`

- 显示从一周前到现在的最近作业：

`sacct --starttime=$(date -d "1 week ago" +'%F')`

- 输出属性的更多字符：

`sacct --format=JobID,JobName%100`