# etcdctl

> 与 `etcd` 交互，`etcd` 是一个高可用性的键值对存储。
> 更多信息：<https://etcd.io/docs/latest/dev-guide/interacting_v3/>。

- 显示与指定键关联的值：

`etcdctl get {{my/key}}`

- 存储一个键值对：

`etcdctl put {{my/key}} {{my_value}}`

- 删除一个键值对：

`etcdctl del {{my/key}}`

- 存储一个键值对，从文件中读取值：

`etcdctl put {{my/file}} < {{path/to/file.txt}}`

- 保存 etcd 键值存储的快照：

`etcdctl snapshot save {{path/to/snapshot.db}}`

- 还原 etcd 键值存储的快照（随后重启 etcd 服务器）：

`etcdctl snapshot restore {{path/to/snapshot.db}}`

- 添加一个用户：

`etcdctl user add {{my_user}}`

- 监视键的变化：

`etcdctl watch {{my/key}}`