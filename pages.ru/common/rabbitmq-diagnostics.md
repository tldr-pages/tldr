# rabbitmq-diagnostics

> Выполнять диагностику, мониторинг и проверки работоспособности узлов RabbitMQ.
> Многие подкоманды делегируются команде `rabbitmqctl`.
> Больше информации: <https://www.rabbitmq.com/docs/man/rabbitmq-diagnostics.8>.

- Вывести список тревог ресурсов:

`rabbitmq-diagnostics alarms`

- Вывести список сертификатов узла:

`rabbitmq-diagnostics certificates`

- Проверить, запущен ли RabbitMQ на указанном узле:

`rabbitmq-diagnostics check_running --node {{узел}}`

- Запустить обнаружение одноранговых узлов:

`rabbitmq-diagnostics discover_peers`

- Вывести список слушателей (привязанных сокетов):

`rabbitmq-diagnostics listeners`

- Вывести последние `n` строк журнала на указанном узле:

`rabbitmq-diagnostics log_tail --number {{n}} --node {{узел}}`
