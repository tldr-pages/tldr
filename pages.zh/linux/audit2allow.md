# audit2allow

> 根据日志中找到的拒绝操作创建 SELinux 本地策略模块。
> 注意：使用 audit2allow 时需谨慎。在应用生成的策略之前，务必对其进行审查，因为它可能会允许过多的访问。
> 更多信息：<https://manned.org/audit2allow>.

- 生成允许所有被拒绝服务访问的本地策略：

`sudo audit2allow --all -M {{local_policy_name}}`

- 从审计日志生成允许特定进程/服务/命令访问的本地策略模块：

`sudo grep {{apache2}} /var/log/audit/audit.log | sudo audit2allow -M {{local_policy_name}}`

- 查看和审查本地策略的类型强制 (.te) 文件：

`vim {{local_policy_name}}.te`

- 安装本地策略模块：

`sudo semodule -i {{local_policy_name}}.pp`
