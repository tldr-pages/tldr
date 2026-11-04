# rabbitmq-streams

> Управлять потоками RabbitMQ.
> Больше информации: <https://www.rabbitmq.com/docs/man/rabbitmq-streams.8>.

- Добавить реплику потока на указанном узле:

`rabbitmq-streams add_replica {{поток}} {{узел}}`

- Удалить реплику потока на указанном узле:

`rabbitmq-streams delete_replica {{поток}} {{узел}}`

- Показать статус потока:

`rabbitmq-streams stream_status {{поток}}`

- Перезапустить поток:

`rabbitmq-streams restart_stream {{поток}}`

- Вывести список подключений потоков:

`rabbitmq-streams list_stream_connections`

- Вывести список всех потребителей потоков:

`rabbitmq-streams list_stream_consumers`

- Вывести список всех издателей потоков:

`rabbitmq-streams list_stream_publishers`

- Вывести информацию отслеживания для потока:

`rabbitmq-streams list_stream_tracking {{поток}}`
