# rabbitmq-upgrade

> Manage the upgrade of a RabbitMQ node.
> More information: <https://www.rabbitmq.com/docs/man/rabbitmq-upgrade.8.html>.

- Wait for all quorum queues to have an above minimum online quorum:

`rabbitmq-upgrade await_online_quorum_plus_one`

- Put the node in maintenance mode:

`rabbitmq-upgrade drain`

- Put the node out of maintenance and into regular operating mode:

`rabbitmq-upgrade revive`

- Run post-upgrade tasks:

`rabbitmq-upgrade post_upgrade`

- Display help:

`rabbitmq-upgrade help`
