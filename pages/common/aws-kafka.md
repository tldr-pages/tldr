# AWS Kafka CLI Commands

> AWS CLI commands for managing Amazon Managed Streaming for Apache Kafka (Amazon MSK).
> More information: <https://docs.aws.amazon.com/cli/latest/reference/kafka/index.html>.

- Create a Kafka Cluster:

`aws kafka create-cluster --cluster-name {{cluster_name}} --broker-node-group-info instanceType={{instance_type}},clientSubnets={{subnet_ids}} --kafka-version {{kafka_version}} --number-of-broker-nodes {{number_of_broker_nodes}}`

- Describe a Kafka Cluster:

`aws kafka describe-cluster --cluster-arn {{cluster_arn}}`

- List Kafka Clusters:

`aws kafka list-clusters`

- Create a Configuration:

`aws kafka create-configuration --name {{configuration_name}} --server-properties {{file://{{path_to_server_properties_file}}`

- Describe Configuration:

`aws kafka describe-configuration --arn <configuration-arn>`

- List Configurations:

`aws kafka list-configurations`

- Update a Kafka Cluster Configuration:

`aws kafka update-cluster-configuration --cluster-arn <cluster-arn> --configuration-info arn=<configuration-arn>,revision=<configuration-revision>`

- Delete a Kafka Cluster:

`aws kafka delete-cluster --cluster-arn {{cluster_arn}}`
