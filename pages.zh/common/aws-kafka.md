# aws kafka

> 管理 Amazon MSK (Managed Streaming for Apache Kafka) 集群。
> 参见: `aws`。
> 更多信息: <https://docs.aws.amazon.com/cli/latest/reference/kafka/index.html>。

- 创建新的 MSK 集群:

`aws kafka create-cluster --cluster-name {{cluster_name}} --broker-node-group-info instanceType={{instance_type}},clientSubnets={{subnet_id1 subnet_id2 ...}} --kafka-version {{version}} --number-of-broker-nodes {{number}}`

- 描述 MSK 集群:

`aws kafka describe-cluster --cluster-arn {{cluster_arn}}`

- 列出当前区域中的所有 MSK 集群:

`aws kafka list-clusters`

- 创建新的 MSK 配置:

`aws kafka create-configuration --name {{configuration_name}} --server-properties file://{{path/to/configuration_file.txt}}`

- 描述 MSK 配置:

`aws kafka describe-configuration --arn {{configuration_arn}}`

- 列出当前区域中的所有 MSK 配置:

`aws kafka list-configurations`

- 更新 MSK 集群配置:

`aws kafka update-cluster-configuration --cluster-arn {{cluster_arn}} --configuration-info arn={{configuration_arn}},revision={{configuration_revision}}`

- 删除 MSK 集群:

`aws kafka delete-cluster --cluster-arn {{cluster_arn}}`