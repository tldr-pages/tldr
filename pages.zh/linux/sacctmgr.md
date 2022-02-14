# sacctmgr

> 查看、配置、管理 Slurm 账户。
> 更多信息：<https://slurm.schedmd.com/sacctmgr.html>.

- 显示现有配置：

`sacctmgr show configuration`

- 向 Slurm 数据库添加集群：

`sacctmgr add cluster {{集群名}}`

- 向 Slurm 数据库添加账户：

`sacctmgr add account {{账户名}} cluster={{账户所在集群}}`

- 以指定格式显示用户、账户资源关联、集群、账户的详细信息：

`sacctmgr show {{user|association|cluster|account}} format="Accout%10" format="GrpTRES%30"`
