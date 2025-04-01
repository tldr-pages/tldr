# knotc

> 控制 Knot DNS 服务器。
> 更多信息：<https://www.knot-dns.cz/docs/latest/html/man_knotc.html>.

- 开始编辑一个区域：

`knotc zone-begin {{zone}}`

- 设置一个 TTL 为 3600 的 A 记录：

`knotc zone-set {{zone}} {{subdomain}} 3600 A {{ip_address}}`

- 完成区域编辑：

`knotc zone-commit {{zone}}`

- 获取当前区域数据：

`knotc zone-read {{zone}}`

- 获取当前服务器配置：

`knotc conf-read server`
