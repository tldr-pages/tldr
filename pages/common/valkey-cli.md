# valkey-cli

> Open a connection to a Valkey server.
> More information: <https://valkey.io/topics/cli/>.
- Connect to the local server:

`valkey-cli`

- Connect to a remote server on the default port (6379):

`valkey-cli -h {{host}}`

- Connect to a remote server specifying a port number:

`valkey-cli -h {{host}} -p {{port}}`

- Connect to a remote server specifying a URI:

`valkey-cli -u {{uri}}`

- Specify a password:

`valkey-cli -a {{password}}`

- Execute valkey command:

`valkey-cli {{valkey_command}}`

- Connect to the local cluster:

`valkey-cli -c`