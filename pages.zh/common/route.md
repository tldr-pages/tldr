# route

> 使用 route 命令设置路由表。
> 更多信息：<https://manned.org/route>。

- 显示路由表信息：

`route -n`

- 添加路由规则：

`sudo route add -net {{ip_address}} netmask {{netmask_address}} gw {{gw_address}}`

- 删除路由规则：

`sudo route del -net {{ip_address}} netmask {{netmask_address}} dev {{gw_address}}`
