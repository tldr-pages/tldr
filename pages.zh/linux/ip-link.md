# ip link

> 管理网络接口。
> 更多信息：<https://manned.org/ip-link>。

- 显示所有网络接口的信息：

`ip link`

- 显示特定网络接口的信息：

`ip link show {{ethN}}`

- 启用或禁用网络接口：

`ip link set {{ethN}} {{up|down}}`

- 给网络接口起一个有意义的名字：

`ip link set {{ethN}} alias "{{LAN Interface}}"`

- 更改网络接口的MAC地址：

`ip link set {{ethN}} address {{ff:ff:ff:ff:ff:ff}}`

- 更改网络接口的MTU大小以使用巨型帧：

`ip link set {{ethN}} mtu {{9000}}`