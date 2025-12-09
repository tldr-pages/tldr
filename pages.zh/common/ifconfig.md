# ifconfig

> 网络接口配置工具。
> 更多信息：<https://net-tools.sourceforge.io/man/ifconfig.8.html>.

- 查看某个网络接口的网络设置：

`ifconfig {{接口名称}}`

- 显示所有接口的详细信息，包括已禁用的接口：

`ifconfig -a`

- 禁用一个接口：

`ifconfig {{接口名称}} down`

- 启用一个接口：

`ifconfig {{接口名称}} up`

- 为一个接口分配 IP 地址：

`ifconfig {{接口名称}} {{IP地址}}`
