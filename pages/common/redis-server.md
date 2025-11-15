# redis-server

> Persistent key-value database.
> More information: <https://redis.io>.

- Start Redis server, using the default port (6379), and write logs to `stdout`:

`redis-server`

- Start Redis server, using the default port, as a background process:

`redis-server --daemonize yes`

- Start Redis server, using the specified port, as a background process:

`redis-server --port {{port}} --daemonize yes`

- Start Redis server with a custom configuration file:

`redis-server {{path/to/redis.conf}}`

- Start Redis server with verbose logging:

`redis-server --loglevel {{warning|notice|verbose|debug}}`
