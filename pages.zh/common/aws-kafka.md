# aws kafka

> 管理 Amazon MSK（Managed Streaming for Apache Kafka）集群。
> 请参阅：`aws`
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/kafka/>.

- 创建一个新的 MSK 集群：

`aws kafka create-cluster --cluster-name {{集群名称}} --broker-node-group-info instanceType={{实例类型}},clientSubnets={{子网 ID1 子网 ID2 ...}} --kafka-version {{版本}} --number-of-broker-nodes {{数量}}`

- 描述一个 MSK 集群：

`aws kafka describe-cluster --cluster-arn {{集群 ARN}}`

- 列出当前区域中的所有 MSK 集群：

`aws kafka list-clusters`

- 创建一个新的 MSK 配置：

`aws kafka create-configuration --name {{配置名称}} --server-properties file://{{路径/到/配置文件.txt}}`

- 描述一个 MSK 配置：

`aws kafka describe-configuration --arn {{配置 ARN}}`

- 列出当前区域中的所有 MSK 配置：

`aws kafka list-configurations`

- 更新 MSK 集群配置：

`aws kafka update-cluster-configuration --cluster-arn {{集群 ARN}} --configuration-info arn={{配置 ARN}},revision={{配置修订版本}}`

- 删除 MSK 集群：

`aws kafka delete-cluster --cluster-arn {{集群 ARN}}`
