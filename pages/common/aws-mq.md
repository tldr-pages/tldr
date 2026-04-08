# aws mq

> Define and operate message brokers in AWS.
> More information: <https://docs.aws.amazon.com/cli/latest/reference/mq/>.

- Create a broker:

`aws mq create-broker --host-instance-type {{instance_type}} --broker-name {{name}} --engine-type [ACTIVEMQ|RABBITMQ] [--publicly-accessible|--no-publicly-accessible]`

- List all brokers:

`aws mq list-brokers`

- Describe broker:

`aws mq describe-broker --broker-id {{broker_id}}`
