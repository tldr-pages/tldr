# rabbitmqctl-vhosts

> Gestiona los hosts virtuales (vhosts) en RabbitMQ.
> Los vhosts se utilizan para separar varios brokers lógicos en el mismo servidor de RabbitMQ.
> Más información: <https://www.rabbitmq.com/docs/vhosts>.

- Muestra todos los hosts virtuales:

`rabbitmqctl list_vhosts`

- Añade un nuevo host virtual:

`rabbitmqctl add_vhost {{vhost_nombre}}`

- Elimina un host virtual:

`rabbitmqctl delete_vhost {{vhost_nombre}}`

- Establece permisos para un usuario en un host virtual específico:

`rabbitmqctl set_permissions {{[-p|--vhost]}} {{vhost_nombre}} {{usuario}} {{read}} {{write}} {{configure}}`

- Borra los permisos de un usuario en un host virtual específico:

`rabbitmqctl clear_permissions {{[-p|--vhost]}} {{vhost_nombre}} {{usuario}}`
