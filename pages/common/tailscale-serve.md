# tailscale serve

> Share a local server, file, or directory with devices on your Tailscale network.
> See also: `tailscale funnel`.
> More information: <https://tailscale.com/docs/reference/tailscale-cli/serve>.

- Expose an HTTP server running at 127.0.0.1:3000 in the foreground:

`tailscale serve 3000`

- Expose an HTTP server running at 127.0.0.1:3000 in the background:

`tailscale serve --bg 3000`

- Expose a local file or directory:

`tailscale serve {{path/to/file_or_directory}}`

- Expose a local server on a specific HTTPS port:

`tailscale serve --https {{8443}} {{localhost:3000}}`

- Stop serving on a specific HTTPS port:

`tailscale serve --https {{443}} off`

- Display the current serve configuration:

`tailscale serve status`

- Display the current serve configuration in JSON format:

`tailscale serve status --json`

- Remove all serve configuration:

`tailscale serve reset`
