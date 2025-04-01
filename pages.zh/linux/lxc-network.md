# lxc network

> 管理 LXD 容器的网络。
> 更多信息：<https://linuxcontainers.org/lxd/docs/master/networks>.

- 列出所有可用网络：

`lxc network list`

- 显示特定网络的配置：

`lxc network show {{network_name}}`

- 将运行中的实例添加到特定网络：

`lxc network attach {{network_name}} {{container_name}}`

- 创建新的托管网络：

`lxc network create {{network_name}}`

- 设置特定网络的桥接接口：

`lxc network set {{network_name}} bridge.external_interfaces {{eth0}}`

- 禁用特定网络的 NAT：

`lxc network set {{network_name}} ipv{{4}}.nat false`