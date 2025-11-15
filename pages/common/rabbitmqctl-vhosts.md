# rabbitmqctl-vhosts

> Manage virtual hosts (vhosts) in RabbitMQ.
> Vhosts are used to separate multiple logical brokers on the same RabbitMQ server.
> More information: <https://www.rabbitmq.com/vhosts.html>.

- List all virtual hosts:

`rabbitmqctl list_vhosts`

- Add a new virtual host:

`rabbitmqctl add_vhost {{vhost_name}}`

- Delete a virtual host:

`rabbitmqctl delete_vhost {{vhost_name}}`

- Set permissions for a user on a specific virtual host:

`rabbitmqctl set_permissions {{[-p|--vhost]}} {{vhost_name}} {{username}} {{read}} {{write}} {{configure}}`

- Clear permissions for a user on a specific virtual host:

`rabbitmqctl clear_permissions {{[-p|--vhost]}} {{vhost_name}} {{username}}`
