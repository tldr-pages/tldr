# nomad

> 分布式、高可用性、数据中心感知的调度器。
> 更多信息：<https://www.nomadproject.io/docs/commands/>.

- 显示集群中节点的状态：

`nomad node status`

- 验证作业文件：

`nomad job validate {{path/to/file.nomad}}`

- 计划作业以在集群上执行：

`nomad job plan {{path/to/file.nomad}}`

- 在集群上运行作业：

`nomad job run {{path/to/file.nomad}}`

- 显示当前在集群上运行的作业状态：

`nomad job status`

- 显示有关特定作业的详细状态信息：

`nomad job status {{job_name}}`

- 跟踪特定分配的日志：

`nomad alloc logs {{alloc_id}}`

- 显示存储卷的状态：

`nomad volume status`