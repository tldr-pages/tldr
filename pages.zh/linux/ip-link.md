# ip link

> 管理网络接口。
> 更多信息：<https://manned.org/ip-link>.

- 显示所有网络接口的信息：

`ip {{[l|link]}}`

- 显示特定网络接口的信息：

`ip {{[l|link]}} {{[sh|show]}} {{ethN}}`

- 启用或禁用网络接口：

`sudo ip {{[l|link]}} {{[s|set]}} {{ethN}} {{up|down}}`

- 为网络接口设置有意义的名称：

`sudo ip {{[l|link]}} {{[s|set]}} {{ethN}} {{[al|alias]}} "{{LAN 接口}}"`

- 更改网络接口的 MAC 地址：

`sudo ip {{[l|link]}} {{[s|set]}} {{ethN}} {{[a|address]}} {{ff:ff:ff:ff:ff:ff}}`

- 将网络接口的 MTU 大小更改为使用巨型帧：

`sudo ip {{[l|link]}} {{[s|set]}} {{ethN}} mtu {{9000}}`

- 设置设备的混杂模式状态：

`sudo ip {{[l|link]}} {{[s|set]}} {{ethN}} promisc {{on|off}}`
