# cidr

> 简化 IPv4/IPv6 CIDR 网络前缀的管理，包括计数、重叠检查、解释和子网划分。
> 更多信息：<https://github.com/bschaatsbergen/cidr>。

- 解释一个 CIDR 范围：

`cidr explain {{10.0.0.0/16}}`

- 检查一个地址是否属于一个 CIDR 范围：

`cidr contains {{10.0.0.0/16}} {{10.0.14.5}}`

- 获取一个 CIDR 范围内的所有地址数量：

`cidr count {{10.0.0.0/16}}`

- 检查两个 CIDR 范围是否重叠：

`cidr overlaps {{10.0.0.0/16}} {{10.0.14.0/22}}`

- 将一个 CIDR 范围划分为指定数量的子网：

`cidr divide {{10.0.0.0/16}} {{9}}`
