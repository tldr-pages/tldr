# rabbitmqctl-cluster

> Управлять узлами RabbitMQ в кластере.
> Больше информации: <https://www.rabbitmq.com/docs/man/rabbitmqctl.8>.

- Показать статус кластера:

`rabbitmqctl cluster_status`

- Показать статус текущего узла:

`rabbitmqctl status`

- Запустить приложение RabbitMQ на конкретном узле:

`rabbitmqctl {{[-n|--node]}} {{имя_узла}} start_app`

- Остановить приложение RabbitMQ на конкретном узле:

`rabbitmqctl {{[-n|--node]}} {{имя_узла}} stop_app`

- Остановить конкретный узел RabbitMQ:

`rabbitmqctl {{[-n|--node]}} {{имя_узла}} stop`

- Сбросить конкретный узел RabbitMQ в чистое состояние:

`rabbitmqctl {{[-n|--node]}} {{имя_узла}} reset`

- Присоединить текущий узел к существующему кластеру:

`rabbitmqctl join_cluster {{имя_узла}}`
