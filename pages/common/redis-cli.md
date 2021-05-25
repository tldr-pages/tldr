# redis-cli

> Opens a connection to a Redis server.
> More information: <https://redis.io/topics/rediscli>.

- Connect to the local server:

`redis-cli`

- Connect to a remote server on the default port (6379):

`redis-cli -h {{host}}`

- Connect to a remote server specifying a port number:

`redis-cli -h {{host}} -p {{port}}`

- Connect to a remote server specifying an URI:

`redis-cli -u {{uri}}`

- Specify a password:

`redis-cli -a {{password}}`

- Execute Redis command:

`redis-cli {{redis_command}}`

- Connect to the local cluster:

`redis-cli -c`
