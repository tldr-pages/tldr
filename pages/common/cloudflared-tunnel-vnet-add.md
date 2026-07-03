# cloudflared tunnel vnet add

> Add a new virtual network to which private IP routes can be attached.
> See also: `cloudflared tunnel vnet`.
> More information: <https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/private-net/>.

- Add a virtual network:

`cloudflared tunnel vnet add {{virtual_network_name}}`

- Add a virtual network with a comment:

`cloudflared tunnel vnet add {{virtual_network_name}} "{{comment}}"`

- Add a virtual network and make it the account default:

`cloudflared tunnel vnet add {{[-d|--default]}} {{virtual_network_name}}`
