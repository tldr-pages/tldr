# http-server

> Simple static HTTP server to serve static files.
> More information: <https://github.com/http-party/http-server>.

- Start an HTTP server listening on the default port to serve the current directory:

`http-server`

- Start an HTTP server on a specific port to serve a specific directory:

`http-server {{path/to/directory}} --port {{port}}`

- Start an HTTP server using basic authentication:

`http-server --username {{username}} --password {{password}}`

- Start an HTTP server with directory listings disabled:

`http-server -d {{false}}`

- Start an HTTPS server on the default port using the specified certificate:

`http-server --ssl --cert {{path/to/cert.pem}} --key {{path/to/key.pem}}`

- Start an HTTP server and include the client's IP address in the output logging:

`http-server --log-ip`

- Start an HTTP server with CORS enabled by including the `Access-Control-Allow-Origin: *` header in all responses:

`http-server --cors`

- Start an HTTP server with logging disabled:

`http-server --silent`
