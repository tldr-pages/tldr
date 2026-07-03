# cloudflared tunnel cleanup

> Delete stale connections for one or more tunnels.
> See also: `cloudflared tunnel delete`.
> More information: <https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/>.

- Clean up connections for a tunnel:

`cloudflared tunnel cleanup {{tunnel_name}}`

- Clean up connections for multiple tunnels:

`cloudflared tunnel cleanup {{tunnel1 tunnel2 ...}}`

- Clean up connections for a single connector by ID:

`cloudflared tunnel cleanup {{[-c|--connector-id]}} {{connector_id}} {{tunnel_name}}`