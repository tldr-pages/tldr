# sacctmgr

> 查看、配置、管理Slurm账户。
> 更多信息：<https://slurm.schedmd.com/sacctmgr.html>。

- 显示现有配置：

`sacctmgr show configuration`

- 向slurm数据库添加集群：

`sacctmgr add cluster {{cluster_name}}`

- 向slurm数据库添加账户：

`sacctmgr add account {{account_name}} cluster={{cluster_of_account}}`

- （以指定格式）显示用户、账户资源关联、集群、账户的详细信息：

`sacctmgr show {{user/association/cluster/account}} [format="Accout%10" format="GrpTRES%30"]`
