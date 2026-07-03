# cloudflared tunnel route ip

> Manage Cloudflare WARP routing to private IP networks exposed through tunnels.
> See also: `cloudflared tunnel route ip add`, `cloudflared tunnel vnet`.
> More information: <https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/>.

- Add a private network route to a tunnel:

`cloudflared tunnel route ip add {{10.0.0.0/8}} {{tunnel_name}}`

- Show the routing table:

`cloudflared tunnel route ip show`

- Check which route matches a given IP:

`cloudflared tunnel route ip get {{10.0.0.1}}`

- Delete a route:

`cloudflared tunnel route ip delete {{10.0.0.0/8}}`