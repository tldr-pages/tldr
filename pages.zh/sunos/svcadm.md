# svcadm

> 操作服务实例。
> 更多信息：<https://www.unix.com/man-page/linux/1m/svcadm>.

- 在服务数据库中启用服务：

`svcadm enable {{service_name}}`

- 禁用服务：

`svcadm disable {{service_name}}`

- 重启正在运行的服务：

`svcadm restart {{service_name}}`

- 指令服务重新读取配置文件：

`svcadm refresh {{service_name}}`

- 清除处于维护状态的服务并指令其启动：

`svcadm clear {{service_name}}`
