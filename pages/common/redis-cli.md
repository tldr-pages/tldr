# redis-cli

> Opens a connection to a Redis server.

- Connect to the local server:

`redis-cli`

- Connect to a remote server on the default port (6379):

`redis-cli -h {{host}}`

- Connect to a remote server specifying a port number:

`redis-cli -h {{host}} -p {{port}}`

- Specify a password:

`redis-cli -a {{password}}`

- Execute Redis command:

`redis-cli {{redis_command}}`
