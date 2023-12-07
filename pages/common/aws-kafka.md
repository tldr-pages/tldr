# AWS Kafka CLI Commands

> AWS CLI commands for managing Amazon Managed Streaming for Apache Kafka (Amazon MSK).
> More information: <https://docs.aws.amazon.com/cli/latest/reference/kafka/index.html>.

- Create a Kafka Cluster:

`aws kafka create-cluster --cluster-name <cluster-name> --broker-node-group-info instanceType=<instance-type>,clientSubnets=<subnet-ids> --kafka-version <kafka-version> --number-of-broker-nodes <number-of-broker-nodes>`

- Describe a Kafka Cluster:

`aws kafka describe-cluster --cluster-arn <cluster-arn>`

- List Kafka Clusters:

`aws kafka list-clusters`

- Create a Configuration:

`aws kafka create-configuration --name <configuration-name> --server-properties file://<path-to-server-properties-file>`

- Describe Configuration:

`aws kafka describe-configuration --arn <configuration-arn>`

- List Configurations:

`aws kafka list-configurations`

- Update a Kafka Cluster Configuration:

`aws kafka update-cluster-configuration --cluster-arn <cluster-arn> --configuration-info arn=<configuration-arn>,revision=<configuration-revision>`

- Delete a Kafka Cluster:

`aws kafka delete-cluster --cluster-arn <cluster-arn>`
