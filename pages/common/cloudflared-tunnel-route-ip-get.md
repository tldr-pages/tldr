# cloudflared tunnel route ip get

> Check which row of the private IP routing table matches a given IP.
> See also: `cloudflared tunnel route ip`.
> More information: <https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/>.

- Check which route matches an IP:

`cloudflared tunnel route ip get {{10.0.0.1}}`

- Check against a specific virtual network's routing table:

`cloudflared tunnel route ip get {{[--vn|--vnet]}} {{virtual_network}} {{10.0.0.1}}`