# sc

> 与服务控制管理器及服务进行通信。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/sc-query>。

- 显示服务的状态（不提供服务名称将列出所有服务）：

`sc.exe query {{service_name}}`

- 异步启动服务：

`sc.exe create {{service_name}} binpath= {{path\to\service_binary_file}}`

- 异步停止服务：

`sc.exe delete {{service_name}}`

- 设置服务的类型：

`sc.exe config {{service_name}} type= {{service_type}}`