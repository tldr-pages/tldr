# knock

> 端口敲击客户端，用于在防火墙上打开特定端口。
> 更多信息：<https://manned.org/knock>.

- 使用不同协议敲击端口：

`knock {{hostname}} {{portnumber}}:{{protocol}}`

- 使用 UDP 敲击端口：

`knock -u {{hostname}} {{portnumber}}`

- 强制使用 IPv4/IPv6：

`knock {{-4|-6}} {{hostname}} {{portnumber}}`

- 显示连接的错误和详细信息：

`knock -v {{hostname}} {{portnumber}}`
