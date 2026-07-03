# cloudflared tunnel info

> Show details about the active connectors for a tunnel.
> See also: `cloudflared tunnel list`.
> More information: <https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/>.

- Show connector details for a tunnel by name or UUID:

`cloudflared tunnel info {{tunnel_name}}`

- Render the output as JSON or YAML:

`cloudflared tunnel info {{[-o|--output]}} {{json|yaml}} {{tunnel_name}}`

- Include recently disconnected connections:

`cloudflared tunnel info --show-recently-disconnected {{tunnel_name}}`

- Sort connections by a specific field:

`cloudflared tunnel info --sort-by {{id|startedAt|numConnections|version}} {{tunnel_name}}`
