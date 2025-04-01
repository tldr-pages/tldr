# sc

> 与服务控制管理器和服务进行通信。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/sc-query>.

- 显示服务的状态（不指定服务名称将列出所有服务）：

`sc.exe query {{service_name}}`

- 异步启动服务：

`sc.exe start {{service_name}}`

- 异步停止服务：

`sc.exe stop {{service_name}}`

- 设置服务类型：

`sc.exe config {{service_name}} type= {{service_type}}`
