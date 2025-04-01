# sreport

> 从会计数据生成关于作业、用户和集群的报告。
> 更多信息：<https://slurm.schedmd.com/sreport.html>.

- 显示由管道分隔的集群利用率数据：

`sreport --parsable cluster utilization`

- 显示运行的作业数量：

`sreport job sizes printjobcount`

- 显示使用 CPU 时间最多的用户：

`sreport user topuser`
