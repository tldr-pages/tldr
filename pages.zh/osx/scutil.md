# scutil

> 管理系统配置参数。
> 设置配置时必须是 root 权限。
> 更多信息：<https://ss64.com/osx/scutil.html>.

- 显示 DNS 配置：

`scutil --dns`

- 显示代理配置：

`scutil --proxy`

- 获取计算机名称：

`scutil --get ComputerName`

- 设置计算机名称：

`sudo scutil --set ComputerName {{我的计算机名}}`

- 获取主机名（HostName）：

`scutil --get HostName`

- 设置主机名：

`scutil --set HostName {{hostname}}`
