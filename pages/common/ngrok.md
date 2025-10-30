# ngrok

> Reverse proxy that creates a secure tunnel from a public endpoint to a locally running web service.
> More information: <https://ngrok.com/docs/agent/cli/>.

- Expose a local HTTP service on a given port:

`ngrok http {{80}}`

- Expose a local HTTP service on a specific host:

`ngrok http {{example.dev}}:{{80}}`

- Expose a local HTTPS server:

`ngrok http https://localhost`

- Expose TCP traffic on a given port:

`ngrok tcp {{22}}`

- Expose TLS traffic for a specific host and port:

`ngrok tls -hostname={{example.com}} {{443}}`
