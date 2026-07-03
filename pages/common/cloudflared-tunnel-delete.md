# cloudflared tunnel delete

> Delete one or more tunnels by name or UUID.
> See also: `cloudflared tunnel cleanup`.
> More information: <https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/>.

- Delete a tunnel (only if it has no active connections):

`cloudflared tunnel delete {{tunnel_name}}`

- Delete a tunnel even if it is connected or has dependencies:

`cloudflared tunnel delete {{[-f|--force]}} {{tunnel_name}}`

- Delete multiple tunnels at once:

`cloudflared tunnel delete {{tunnel1 tunnel2 ...}}`