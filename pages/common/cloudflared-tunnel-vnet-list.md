# cloudflared tunnel vnet list

> List the virtual networks in your Cloudflare account.
> See also: `cloudflared tunnel vnet`.
> More information: <https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/private-net/>.

- List all virtual networks:

`cloudflared tunnel vnet list`

- Filter by name:

`cloudflared tunnel vnet list --name {{virtual_network_name}}`

- Show only the default virtual network:

`cloudflared tunnel vnet list --is-default`

- Output as JSON or YAML:

`cloudflared tunnel vnet list {{[-o|--output]}} {{json|yaml}}`