# cloudflared tunnel vnet

> Configure and query virtual networks to manage private IP routes with overlapping IPs.
> See also: `cloudflared tunnel vnet add`, `cloudflared tunnel route ip`.
> More information: <https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/private-net/>.

- Add a virtual network:

`cloudflared tunnel vnet add {{virtual_network_name}} "{{comment}}"`

- List virtual networks:

`cloudflared tunnel vnet list`

- Update a virtual network:

`cloudflared tunnel vnet update {{virtual_network_name}}`

- Delete a virtual network:

`cloudflared tunnel vnet delete {{virtual_network_name}}`