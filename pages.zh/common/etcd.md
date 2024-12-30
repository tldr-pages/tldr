# etcd

> 一个分布式、可靠的键值存储，用于分布式系统中最关键的数据。
> 更多信息：<https://etcd.io>。

- 启动单节点 etcd 集群：

`etcd`

- 启动单节点 etcd 集群，在自定义 URL 上监听客户端请求：

`etcd --advertise-client-urls {{http://127.0.0.1:1234}} --listen-client-urls {{http://127.0.0.1:1234}}`

- 启动单节点 etcd 集群，使用自定义名称：

`etcd --name {{my_etcd_cluster}}`

- 启动单节点 etcd 集群，并在 <http://localhost:2379/debug/pprof/> 上提供丰富的指标：

`etcd --enable-pprof --metrics extensive`