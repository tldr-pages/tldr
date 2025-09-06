# aws kafka

> Manage an Amazon MSK (Managed Streaming for Apache Kafka) cluster.
> See also: `aws`.
> More information: <https://docs.aws.amazon.com/cli/latest/reference/kafka/index.html>.

- Create a new MSK cluster:

`aws kafka create-cluster --cluster-name {{cluster_name}} --broker-node-group-info instanceType={{instance_type}},clientSubnets={{subnet_id1 subnet_id2 ...}} --kafka-version {{version}} --number-of-broker-nodes {{number}}`

- Describe a MSK cluster:

`aws kafka describe-cluster --cluster-arn {{cluster_arn}}`

- List all MSK clusters in the current region:

`aws kafka list-clusters`

- Create a new MSK configuration:

`aws kafka create-configuration --name {{configuration_name}} --server-properties file://{{path/to/configuration_file.txt}}`

- Describe a MSK configuration:

`aws kafka describe-configuration --arn {{configuration_arn}}`

- List all MSK configurations in the current region:

`aws kafka list-configurations`

- Update the MSK cluster configuration:

`aws kafka update-cluster-configuration --cluster-arn {{cluster_arn}} --configuration-info arn={{configuration_arn}},revision={{configuration_revision}}`

- Delete the MSK cluster:

`aws kafka delete-cluster --cluster-arn {{cluster_arn}}`
