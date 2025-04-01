# sh5util

> 合并由 `sacct_gather_profile` 插件生成的 HDF5 文件。
> 更多信息：<https://slurm.schedmd.com/sh5util.html>。

- 合并指定作业或步骤的每个分配节点上生成的 HDF5 文件：

`sh5util --jobs={{job_id|job_id.step_id}}`

- 从合并的作业文件中提取一个或多个数据序列：

`sh5util --jobs={{job_id|job_id.step_id}} --extract -i {{path/to/file.h5}} --series={{Energy|Filesystem|Network|Task}}`

- 从合并的作业文件中提取所有节点的一个数据项：

`sh5util --jobs={{job_id|job_id.step_id}} --item-extract --series={{Energy|Filesystem|Network|Task}} --data={{data_item}}`
