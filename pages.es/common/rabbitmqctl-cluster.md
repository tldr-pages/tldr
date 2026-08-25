# rabbitmqctl-cluster

> Gestiona los nodos de RabbitMQ en un clúster.
> Más información: <https://www.rabbitmq.com/docs/man/rabbitmqctl.8>.

- Muestra el estado del clúster:

`rabbitmqctl cluster_status`

- Muestra el estado del nodo actual:

`rabbitmqctl status`

- Inicia la aplicación RabbitMQ en un nodo específico:

`rabbitmqctl {{[-n|--node]}} {{nombre_del_nodo}} start_app`

- Detiene la aplicación RabbitMQ en un nodo específico:

`rabbitmqctl {{[-n|--node]}} {{nombre_del_nodo}} stop_app`

- Detiene un nodo RabbitMQ específico:

`rabbitmqctl {{[-n|--node]}} {{nombre_del_nodo}} stop`

- Restablecer un nodo RabbitMQ específico a un estado limpio:

`rabbitmqctl {{[-n|--node]}} {{nombre_del_nodo}} reset`

- Hace que el nodo actual se una a un clúster existente:

`rabbitmqctl join_cluster {{nombre_del_nodo}}`
