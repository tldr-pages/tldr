# rabbitmqctl-cluster

> Manage RabbitMQ nodes in a cluster.
> More information: <https://www.rabbitmq.com/rabbitmqctl.8.html>.

- Display the status of the cluster:

`rabbitmqctl cluster_status`

- Display the status of the current node:

`rabbitmqctl status`

- Start the RabbitMQ application on a specific node:

`rabbitmqctl {{[-n|--node]}} {{nodename}} start_app`

- Stop the RabbitMQ application on a specific node:

`rabbitmqctl {{[-n|--node]}} {{nodename}} stop_app`

- Stop a specific RabbitMQ node:

`rabbitmqctl {{[-n|--node]}} {{nodename}} stop`

- Reset a specific RabbitMQ node to a clean state:

`rabbitmqctl {{[-n|--node]}} {{nodename}} reset`

- Make the current node join an existing cluster:

`rabbitmqctl join_cluster {{nodename}}`
