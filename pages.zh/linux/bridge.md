# bridge

> 显示和操作网络桥接地址和设备。
> 更多信息：<https://manned.org/bridge>.

- 列出所有桥及其接口：

`bridge {{[l|link]}}`

- 显示端口 VLAN 信息：

`bridge {{[v|vlan]}}`

- 将 VLAN 分配给端口：

`sudo bridge {{[v|vlan]}} {{[a|add]}} dev {{lanX}} vid {{vlan_id}} pvid {{tagged|untagged}}`

- 从端口移除 VLAN：

`sudo bridge {{[v|vlan]}} {{[d|delete]}} dev {{lanX}} vid {{vlan_id}}`

- 监视桥接接口的变化：

`bridge {{[mo|monitor]}}`

- 显示帮助：

`bridge {{[h|help]}}`
