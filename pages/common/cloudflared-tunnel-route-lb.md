# cloudflared tunnel route lb

> Use a tunnel as a Cloudflare Load Balancer origin, creating the pool and load balancer if needed.
> See also: `cloudflared tunnel route`.
> More information: <https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/>.

- Route a load balancer hostname to a tunnel, using or creating the given pool:

`cloudflared tunnel route lb {{tunnel_name}} {{hostname.example.com}} {{pool_name}}`