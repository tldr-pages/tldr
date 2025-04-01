# az redis

> 管理 Redis 缓存。
> `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/redis>.

- 创建新的 Redis 缓存实例：

`az redis create --location {{location}} --name {{name}} --resource-group {{resource_group}} --sku {{Basic|Premium|Standard}} --vm-size {{c0|c1|c2|c3|c4|c5|c6|p1|p2|p3|p4|p5}}`

- 更新 Redis 缓存：

`az redis update --name {{name}} --resource-group {{resource_group}} --sku {{Basic|Premium|Standard}} --vm-size {{c0|c1|c2|c3|c4|c5|c6|p1|p2|p3|p4|p5}}`

- 导出 Redis 缓存中的数据：

`az redis export --container {{container}} --file-format {{file-format}} --name {{name}} --prefix {{prefix}} --resource-group {{resource_group}}`

- 删除 Redis 缓存：

`az redis delete --name {{name}} --resource-group {{resource_group}} --yes`