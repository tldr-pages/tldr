# valkey-cli

> Abrir una conexión a un servidor Valkey.
> Más información: <https://valkey.io/topics/cli/>.

- Conectar al servidor local:

`valkey-cli`

- Conectar a un servidor remoto en el puerto predeterminado (6379):

`valkey-cli -h {{host}}`

- Conectar a un servidor remoto especificando un número de puerto:

`valkey-cli -h {{host}} -p {{puerto}}`

- Conectar a un servidor remoto especificando una URI:

`valkey-cli -u {{uri}}`

- Especificar una contraseña:

`valkey-cli -a {{contraseña}}`

- Ejecutar un comando de Valkey:

`valkey-cli {{comando_valkey}}`

- Conectar al clúster local:

`valkey-cli -c`
