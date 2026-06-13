# zeroclaw daemon

> Start the full autonomous runtime for ZeroClaw (gateway + channels + heartbeat).
> More information: <https://github.com/zeroclaw-labs/zeroclaw#quick-start>.

- Start the daemon on default port (8080):

`zeroclaw daemon`

- Start the daemon on a specific port:

`zeroclaw daemon {{[-p|--port]}} {{8080}}`

- Start the daemon on a random available port:

`zeroclaw daemon {{[-p|--port]}} 0`

- Start the daemon on a specific host:

`zeroclaw daemon --host {{0.0.0.0}} {{[-p|--port]}} {{8080}}`

- Display help:

`zeroclaw daemon {{[-h|--help]}}`
