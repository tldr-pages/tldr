# etcd

> 分布式，可靠的键值存储，用于分布式系统中存储最关键的数据。
> 更多信息：<https://etcd.io>.

- 启动单节点 etcd 集群：

`etcd`

- 启动一个单节点 etcd 集群，在自定义 URL 上侦听客户端请求：

`etcd --advertise-client-urls {{http://127.0.0.1:1234}} --listen-client-urls {{http://127.0.0.1:1234}}`

- 使用自定义名称启动单节点 etcd 集群：

`etcd --name {{my_etcd_cluster}}`

- 启动单节点 etcd 集群，同时可以在这里看到大量监控指标 http://localhost:2379/debug/pprof/:

`etcd --enable-pprof --metrics extensive`
