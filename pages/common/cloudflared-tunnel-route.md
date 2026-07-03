# cloudflared tunnel route

> Define which traffic from the Cloudflare edge is routed to a tunnel.
> See also: `cloudflared tunnel route dns`, `cloudflared tunnel route lb`, `cloudflared tunnel route ip`.
> More information: <https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/>.

- Route a DNS hostname to a tunnel:

`cloudflared tunnel route dns {{tunnel_name}} {{hostname.example.com}}`

- Route a Cloudflare Load Balancer to a tunnel:

`cloudflared tunnel route lb {{tunnel_name}} {{hostname.example.com}} {{pool_name}}`

- Route a private IP network (CIDR) to a tunnel:

`cloudflared tunnel route ip add {{10.0.0.0/8}} {{tunnel_name}}`