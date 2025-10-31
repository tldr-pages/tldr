# rabbitmq-streams

> Manage RabbitMQ streams.
> More information: <https://www.rabbitmq.com/docs/man/rabbitmq-streams.8.html>.

- Add a stream replica on the specified node:

`rabbitmq-streams add_replica {{stream}} {{node}}`

- Delete a stream replica on the specified node:

`rabbitmq-streams delete_replica {{stream}} {{node}}`

- Display the status of a stream:

`rabbitmq-streams stream_status {{stream}}`

- Restart a stream:

`rabbitmq-streams restart_stream {{stream}}`

- List stream connections:

`rabbitmq-streams list_stream_connections`

- List all stream consumers:

`rabbitmq-streams list_stream_consumers`

- List all stream publishers:

`rabbitmq-streams list_stream_publishers`

- List tracking information for a stream:

`rabbitmq-streams list_stream_tracking {{stream}}`
