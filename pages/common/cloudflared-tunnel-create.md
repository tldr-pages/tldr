# cloudflared tunnel create

> Create a new tunnel, register it with the Cloudflare edge, and generate its credentials file.
> See also: `cloudflared tunnel run`, `cloudflared tunnel route`.
> More information: <https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/>.

- Create a new named tunnel:

`cloudflared tunnel create {{tunnel_name}}`

- Write the credentials to a specific file:

`cloudflared tunnel create --credentials-file {{path/to/credentials.json}} {{tunnel_name}}`

- Create a tunnel with a specific Base64-encoded secret:

`cloudflared tunnel create {{[-s|--secret]}} {{secret}} {{tunnel_name}}`

- Print the created tunnel details as JSON:

`cloudflared tunnel create {{[-o|--output]}} json {{tunnel_name}}`
