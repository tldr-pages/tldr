# rabbitmq-queues

> Manage RabbitMQ queues.
> More information: <https://www.rabbitmq.com/docs/man/rabbitmq-queues.8.html>.

- Grow quorum queue clusters by adding a member on the specified node:

`rabbitmq-queues grow {{node}} {{all|even}}`

- Rebalance leaders of replicated queues across nodes:

`rabbitmq-queues rebalance {{all|quorum|stream}}`

- Shrink quorum queue clusters by removing any members on the specified node:

`rabbitmq-queues shrink {{node}}`

- Add a quorum queue member on the specified node:

`rabbitmq-queues add_member {{queue}} {{node}}`

- Delete a quorum queue member on the specified node:

`rabbitmq-queues delete_member {{queue}} {{node}}`

- Display quorum status of a quorum queue:

`rabbitmq-queues quorum_status {{queue}}`
