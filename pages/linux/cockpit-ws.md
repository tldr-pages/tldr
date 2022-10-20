# cockpit-ws

> Communicate between the browser application and various configuration tools and services like `cockpit-bridge`.
> More information: <https://cockpit-project.org/guide/latest/cockpit-ws.8.html>.

- Check which certificate `cockpit-ws` will use:

`cockpit-ws --local-ssh`

- Serve HTTP requests to a specific PORT instead of port `9090`:

`cockpit-ws --port {{PORT}}`

- Bind to a specific ADDRESS instead of binding to all available addresses:

`cockpit-ws --address {{ADDRESS}}`

- Don't use TLS:

`cockpit-ws --no-tls`

- Display help:

`cockpit-ws --help`
