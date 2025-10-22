# valkey-server

> In-Memory key-value database.
> More information: <https://valkey.io/topics/server/>.

- Start Valkey server, using the default port (6379), and write logs to `stdout`:

`valkey-server`

- Start Valkey server, using the default port, as a background process:

`valkey-server --daemonize yes`

- Start Valkey server, using the specified port, as a background process:

`valkey-server --port {{port}} --daemonize yes`

- Start Valkey server with a custom configuration file:

`valkey-server {{path/to/valkey.conf}}`

- Start Valkey server with verbose logging:

`valkey-server --loglevel {{warning|notice|verbose|debug}}`
