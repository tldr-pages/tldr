# cloudflared tunnel route ip add

> Add a private IP network (CIDR) to the routing table, reachable through a tunnel.
> See also: `cloudflared tunnel route ip`.
> More information: <https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/>.

- Add a network route to a tunnel:

`cloudflared tunnel route ip add {{10.0.0.0/8}} {{tunnel_name}}`

- Add a route with a descriptive comment:

`cloudflared tunnel route ip add {{10.0.0.0/8}} {{tunnel_name}} "{{comment}}"`

- Add a route to a specific virtual network:

`cloudflared tunnel route ip add {{[--vn|--vnet]}} {{virtual_network}} {{10.0.0.0/8}} {{tunnel_name}}`