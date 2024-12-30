# brctl

> 以太网桥接管理。
> 更多信息：<https://manned.org/brctl>。

- 显示当前存在的以太网桥的列表信息：

`sudo brctl show`

- 创建一个新的以太网桥接口：

`sudo brctl add {{bridge_name}}`

- 删除一个现有的以太网桥接口：

`sudo brctl del {{bridge_name}}`

- 将一个接口添加到现有桥接中：

`sudo brctl addif {{bridge_name}} {{interface_name}}`

- 从现有桥接中移除一个接口：

`sudo brctl delif {{bridge_name}} {{interface_name}}`