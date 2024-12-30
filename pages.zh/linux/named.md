# named

> 执行 DNS（动态名称服务）服务器守护进程，将主机名转换为 IP 地址，反之亦然。
> 更多信息：<https://manned.org/named>。

- 读取默认配置文件 `/etc/named.conf`，读取任何初始数据并监听查询：

`named`

- 读取自定义配置文件：

`named -c {{path/to/named.conf}}`

- 仅使用 IPv4 或 IPv6，即使主机可以使用其他协议：

`named {{-4|-6}}`

- 在特定端口上监听查询，而不是默认的 53 端口：

`named -p {{port}}`

- 在前台运行服务器，不进行守护化：

`named -f`