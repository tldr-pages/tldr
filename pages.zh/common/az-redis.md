# az redis

> 管理 Redis 缓存。
> 属于 `azure-cli`（也称为 `az`）。
> 更多信息：<https://learn.microsoft.com/cli/azure/redis>.

- 创建一个新的 Redis 缓存实例：

`az redis create --location {{位置}} {{[-n|--name]}} {{名称}} {{[-g|--resource-group]}} {{资源组}} --sku {{Basic|Premium|Standard}} --vm-size {{c0|c1|c2|c3|c4|c5|c6|p1|p2|p3|p4|p5}}`

- 更新一个 Redis 缓存：

`az redis update {{[-n|--name]}} {{名称}} {{[-g|--resource-group]}} {{资源组}} --sku {{Basic|Premium|Standard}} --vm-size {{c0|c1|c2|c3|c4|c5|c6|p1|p2|p3|p4|p5}}`

- 导出存储在 Redis 缓存中的数据：

`az redis export --container {{容器}} --file-format {{文件格式}} {{[-n|--name]}} {{名称}} --prefix {{前缀}} {{[-g|--resource-group]}} {{资源组}}`

- 删除一个 Redis 缓存：

`az redis delete {{[-n|--name]}} {{名称}} {{[-g|--resource-group]}} {{资源组}} {{[-y|--yes]}}`
