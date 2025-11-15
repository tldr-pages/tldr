# xcaddy

> The custom build tool for the Caddy Web Server.
> More information: <https://github.com/caddyserver/xcaddy>.

- Build Caddy server from source:

`xcaddy build`

- Build Caddy server with a specific version (defaults to latest):

`xcaddy build {{version}}`

- Build Caddy with a specific module:

`xcaddy build --with {{module_name}}`

- Build Caddy and output to a specific file:

`xcaddy build --output {{path/to/file}}`

- Build and run Caddy for a development plugin in the current directory:

`xcaddy run`

- Build and run Caddy for a development plugin using a specific Caddy config:

`xcaddy run --config {{path/to/file}}`
