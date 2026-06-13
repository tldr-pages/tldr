# lt

> Localtunnel exposes your localhost to the world for easy testing and sharing.
> More information: <https://github.com/localtunnel/localtunnel>.

- Start tunnel from a specific port:

`lt {{[-p|--port]}} {{8000}}`

- Specify the upstream server doing the forwarding:

`lt {{[-p|--port]}} {{8000}} {{[-h|--host]}} {{host}}`

- Request a specific subdomain:

`lt {{[-p|--port]}} {{8000}} {{[-s|--subdomain]}} {{subdomain}}`

- Print basic request info:

`lt {{[-p|--port]}} {{8000}} --print-requests`

- Open the tunnel URL in the default web browser:

`lt {{[-p|--port]}} {{8000}} {{[-o|--open]}}`
