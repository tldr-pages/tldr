# audit2allow

> 创建一个SELinux本地策略模块，以允许基于日志中发现的被拒绝操作的规则。
> 注意：使用audit2allow时请谨慎——在应用生成的策略之前总是要进行审核，因为它可能会允许过多的访问。
> 更多信息：<https://manned.org/audit2allow>。

- 生成一个本地策略，以允许所有被拒绝的服务访问：

`sudo audit2allow --all -M {{local_policy_name}}`

- 生成一个本地策略模块，以从审计日志授予特定进程/服务/命令访问权限：

`sudo grep {{apache2}} /var/log/audit/audit.log | sudo audit2allow -M {{local_policy_name}}`

- 检查并审查本地策略的类型强制 (.te) 文件：

`vim {{local_policy_name}}.te`

- 安装本地策略模块：

`sudo semodule -i {{local_policy_name}}.pp`