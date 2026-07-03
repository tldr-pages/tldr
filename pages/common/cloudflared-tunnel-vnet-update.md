# cloudflared tunnel vnet update

> Update an existing virtual network.
> See also: `cloudflared tunnel vnet`.
> More information: <https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/private-net/>.

- Rename a virtual network:

`cloudflared tunnel vnet update {{[-n|--name]}} {{new_name}} {{virtual_network_name}}`

- Update the comment of a virtual network:

`cloudflared tunnel vnet update {{[-c|--comment]}} "{{comment}}" {{virtual_network_name}}`

- Make a virtual network the account default:

`cloudflared tunnel vnet update {{[-d|--default]}} {{virtual_network_name}}`