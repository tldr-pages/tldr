# consul-kv

> 具有健康检查和服务发现功能的分布式键值存储。
> 更多信息：<https://learn.hashicorp.com/consul/getting-started/kv>。

- 从键值存储中读取一个值：

`consul kv get {{key}}`

- 存储一个新的键值对：

`consul kv put {{key}} {{value}}`

- 删除一个键值对：

`consul kv delete {{key}}`