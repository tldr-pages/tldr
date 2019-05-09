# ngrok

> Reverse proxy that creates a secure tunnel from a public endpoint to a locally running web service.
> Homepage: <ngrok.com>.

- Expose local http service on a given port:

`ngrok http {{80}}`

- Expose local http service on specific host:

`ngrok http {{foo.dev}}:{{80}}`

- Expose a local https server:

`ngrok http https://localhost`

- Expose TCP traffic on a given port:

`ngrok tcp {{22}}`

- Expose TLS traffic for specific host and port:

`ngrok tls -hostname={{foo.com}} {{443}}`

