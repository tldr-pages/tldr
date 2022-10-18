# cockpit-ws

> Used for communication between the browser application and various configuration tools and services like cockpit-bridge.
> More information: <https://cockpit-project.org/guide/latest/cockpit-ws.8.html>.

- To check which certificate cockpit-ws will use run:

`sudo remotectl certificate`

- Show help options:

`cockpit-ws --help`

- Authenticate via SSH at 127.0.0.1 port 22:

`cockpit-ws --local-ssh`

- Serve HTTP requests PORT instead of port 9090:

`cockpit-ws --port PORT`

- Bind to address ADDRESS instead of binding to all available addresses:

`cockpit-ws --address ADDRESS`

- Don't use TLS:

`cockpit-ws --no-tls`

