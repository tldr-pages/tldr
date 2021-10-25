# http-server

> Simple static HTTP server to serve static files.
> More information: <https://github.com/http-party/http-server>.

- Start a HTTP server in the default port to serve the current directory:

`http-server`

- Start a HTTP server in a specific port to serve files from a specific directory:

`http-server {{path/to/directory}} --port {{port}}`

- Start a HTTP server using basic authentication:

`http-server --username {{username}} --password {{password}}`

- Start a HTTP server with directory listings disabled:

`http-server -d {{false}}`

- Start a HTTP server in the default port with SSL using the specified certificates:

`http-server --ssl --cert {{path/to/cert.pem}} --key {{path/to/key.pem}}`

- Start a HTTP server and include the client's IP in the output logging:

`http-server --log-ip`

- Start a HTTP server with CORS enabled via the `Access-Control-Allow-Origin: *` header:

`http-server --cors`

- Start a HTTP server with log messages disabled:

`http-server --silent`
