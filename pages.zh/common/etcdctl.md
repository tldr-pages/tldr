# etcdctl

> 与 `etcd` 高可用键值存储进行交互。
> 更多信息：<https://etcd.io/docs/latest/dev-guide/interacting_v3/>.

- 显示指定键关联的值：

`etcdctl get {{my/key}}`

- 存储一个键值对：

`etcdctl put {{my/key}} {{my_value}}`

- 删除一个键值对：

`etcdctl del {{my/key}}`

- 存储一个键值对，从文件中读取值：

`etcdctl put {{my/file}} < {{path/to/file.txt}}`

- 保存 etcd 键值存储的快照：

`etcdctl snapshot save {{path/to/snapshot.db}}`

- 恢复 etcd 键值存储的快照（之后重启 etcd 服务器）：

`etcdctl snapshot restore {{path/to/snapshot.db}}`

- 添加用户：

`etcdctl user add {{my_user}}`

- 监视键的变化：

`etcdctl watch {{my/key}}`