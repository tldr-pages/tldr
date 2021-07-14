# caddy

> A powerful, enterprise-ready, open source web server with automatic HTTPS, written in Go.
> More information: <https://caddyserver.com>.

- Start Caddy in the foreground:

`caddy run`

- Start Caddy with the specified Caddyfile:

`caddy run --config {{path/to/Caddyfile}}`

- Start Caddy in the background:

`caddy start`

- Stop a background Caddy process:

`caddy stop`

- Run a simple file server on the specified port with a browsable interface:

`caddy file-server --listen :{{8000}} --browse`

- Run a reverse proxy server:

`caddy reverse-proxy --from :{{80}} --to localhost:{{8000}}`
