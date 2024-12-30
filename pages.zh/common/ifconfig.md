# ifconfig

> 网络接口配置工具。
> 更多信息：<https://net-tools.sourceforge.io/man/ifconfig.8.html>。

- 查看接口的网络设置：

`ifconfig {{interface_name}}`

- 显示所有接口的详细信息，包括禁用的接口：

`ifconfig -a`

- 禁用一个接口：

`ifconfig {{interface_name}} down`

- 启用一个接口：

`ifconfig {{interface_name}} up`

- 为接口分配一个IP地址：

`ifconfig {{interface_name}} {{ip_address}}`