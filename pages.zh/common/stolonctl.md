# stolonctl

> Stolon的命令行工具，一个用于PostgreSQL高可用性的云原生PostgreSQL管理器。
> 更多信息：<https://github.com/sorintlab/stolon>。

- 获取集群状态：

`stolonctl --cluster-name {{cluster_name}} --store-backend {{store_backend}} --store-endpoints {{store_endpoints}} status`

- 获取集群数据：

`stolonctl --cluster-name {{cluster_name}} --store-backend {{store_backend}} --store-endpoints {{store_endpoints}} clusterdata`

- 获取集群规范：

`stolonctl --cluster-name {{cluster_name}} --store-backend {{store_backend}} --store-endpoints {{store_endpoints}} spec`

- 使用JSON格式的补丁更新集群规范：

`stolonctl --cluster-name {{cluster_name}} --store-backend {{store_backend}} --store-endpoints {{store_endpoints}} update --patch '{{cluster_spec}}'`