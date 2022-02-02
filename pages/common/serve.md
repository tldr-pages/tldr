# serve

> Static file serving and directory listing.
> More information: <https://github.com/vercel/serve>.

- Start an HTTP server listening on the default port to serve the current directory:

`serve`

- Start an HTTP server on a specific [p]ort to serve a specific directory:

`serve -p {{port}} {{path/to/directory}}`

- Start an HTTP server with CORS enabled by including the `Access-Control-Allow-Origin: *` header in all responses:

`serve --cors`

- Start an HTTP server on the default port rewriting all not-found requests to the `index.html` file:

`serve --single`

- Start an HTTPS server on the default port using the specified certificate:

`serve --ssl-cert {{path/to/cert.pem}} --ssl-key {{path/to/key.pem}}`

- Start an HTTP server on the default port using a specific configuration file:

`serve --config {{path/to/serve.json}}`

- Display help:

`serve --help`
