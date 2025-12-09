# rabbitmq-diagnostics

> Diagnose, monitor, and run health checks on RabbitMQ nodes.
> Many subcommands are delegated to `rabbitmqctl`.
> More information: <https://www.rabbitmq.com/docs/man/rabbitmq-diagnostics.8.html>.

- List resource alarms:

`rabbitmq-diagnostics alarms`

- List node certificates:

`rabbitmq-diagnostics certificates`

- Check if RabbitMQ is running on the specified node:

`rabbitmq-diagnostics check_running --node {{node}}`

- Run peer discovery:

`rabbitmq-diagnostics discover_peers`

- List listeners (bound sockets):

`rabbitmq-diagnostics listeners`

- Print the last `n` log lines on the specified node:

`rabbitmq-diagnostics log_tail --number {{n}} --node {{node}}`
