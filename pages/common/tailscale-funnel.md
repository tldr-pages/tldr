# tailscale funnel

> Share a local server on the internet using Tailscale.
> More information: <https://tailscale.com/kb/1311/tailscale-funnel>.

- Expose a local file in the foreground:

`tailscale funnel {{path/to/file}}`

- Expose a local folder in the foreground:

`tailscale funnel {{path/to/directory}}`

- Expose an HTTP server running at 127.0.0.1:3000 in the foreground:

`tailscale funnel 3000`

- Expose an HTTP server running at 127.0.0.1:3000 in the background:

`tailscale funnel --bg 3000`

- Expose an HTTPS server with invalid or self-signed certificates at https://localhost:8443:

`tailscale funnel https+insecure://localhost:8443`
