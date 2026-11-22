# rabbitmq-queues

> Управлять очередями RabbitMQ.
> Больше информации: <https://www.rabbitmq.com/docs/man/rabbitmq-queues.8>.

- Расширить кластеры очередей кворума, добавив участника на указанном узле:

`rabbitmq-queues grow {{узел}} {{all|even}}`

- Перераспределить лидеров реплицированных очередей между узлами:

`rabbitmq-queues rebalance {{all|quorum|stream}}`

- Сократить кластеры очередей кворума, удалив участников на указанном узле:

`rabbitmq-queues shrink {{узел}}`

- Добавить участника очереди кворума на указанном узле:

`rabbitmq-queues add_member {{очередь}} {{узел}}`

- Удалить участника очереди кворума на указанном узле:

`rabbitmq-queues delete_member {{очередь}} {{узел}}`

- Показать статус кворума для очереди кворума:

`rabbitmq-queues quorum_status {{очередь}}`
