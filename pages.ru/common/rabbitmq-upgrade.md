# rabbitmq-upgrade

> Управлять обновлением узла RabbitMQ.
> Больше информации: <https://www.rabbitmq.com/docs/man/rabbitmq-upgrade.8>.

- Дождаться, пока все очереди кворума получат онлайн-кворум выше минимального:

`rabbitmq-upgrade await_online_quorum_plus_one`

- Перевести узел в режим обслуживания:

`rabbitmq-upgrade drain`

- Вывести узел из режима обслуживания в обычный рабочий режим:

`rabbitmq-upgrade revive`

- Выполнить задачи после обновления:

`rabbitmq-upgrade post_upgrade`

- Показать справку:

`rabbitmq-upgrade help`
