# rabbitmqctl-users

> Gestiona los usuarios de RabbitMQ, sus permisos y sus etiquetas.
> Más información: <https://www.rabbitmq.com/docs/management>.

- Muestra todos los usuarios:

`rabbitmqctl list_users`

- Añade un nuevo usuario con contraseña:

`rabbitmqctl add_user {{usuario}} {{contraseña}}`

- Elimina un usuario existente:

`rabbitmqctl delete_user {{usuario}}`

- Cambia la contraseña de un usuario:

`rabbitmqctl change_password {{usuario}} {{nueva_contraseña}}`

- Establece permisos para un usuario en un host virtual específico:

`rabbitmqctl set_permissions {{[-p|--vhost]}} {{vhost}} {{usuario}} {{read}} {{write}} {{configure}}`

- Borra todos los permisos de un usuario en un host virtual específico:

`rabbitmqctl clear_permissions {{[-p|--vhost]}} {{vhost}} {{usuario}}`

- Asigna una o más etiquetas (por ejemplo, administrador) a un usuario:

`rabbitmqctl set_user_tags {{usuario}} {{etiqueta1 etiqueta2 ...}}`
