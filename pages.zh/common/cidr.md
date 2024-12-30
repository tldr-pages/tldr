# cidr

> 简化 IPv4/IPv6 CIDR 网络前缀管理，提供计数、重叠检查、解释和细分功能。
> 更多信息: <https://github.com/bschaatsbergen/cidr>。

- 解释一个 CIDR 范围：

`cidr explain {{10.0.0.0/16}}`

- 检查一个地址是否属于某个 CIDR 范围：

`cidr contains {{10.0.0.0/16}} {{10.0.14.5}}`

- 获取 CIDR 范围内所有地址的数量：

`cidr count {{10.0.0.0/16}}`

- 检查两个 CIDR 范围是否重叠：

`cidr overlaps {{10.0.0.0/16}} {{10.0.14.0/22}}`

- 将一个 CIDR 范围划分为特定数量的网络：

`cidr divide {{10.0.0.0/16}} {{9}}`