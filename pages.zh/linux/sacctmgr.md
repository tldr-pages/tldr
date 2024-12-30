# sacctmgr

> 查看、设置和管理 Slurm 账户。
> 更多信息：<https://slurm.schedmd.com/sacctmgr.html>。

- 显示当前配置：

`sacctmgr show configuration`

- 向 slurm 数据库添加集群：

`sacctmgr add cluster {{cluster_name}}`

- 向 slurm 数据库添加账户：

`sacctmgr add account {{account_name}} cluster={{cluster_of_account}}`

- 使用特定格式显示用户/关联/集群/账户的详细信息：

`sacctmgr show {{user|association|cluster|account}} format="Account%10" format="GrpTRES%30"`