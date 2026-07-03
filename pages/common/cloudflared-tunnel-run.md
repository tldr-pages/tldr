# cloudflared tunnel run

> Run a tunnel, creating connections between your server and the Cloudflare edge.
> See also: `cloudflared tunnel create`, `cloudflared tunnel cleanup`.
> More information: <https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/>.

- Run a tunnel by name or UUID:

`cloudflared tunnel run {{tunnel_name}}`

- Run a tunnel using a specific configuration file:

`cloudflared tunnel --config {{path/to/config.yml}} run {{tunnel_name}}`

- Run a tunnel using its token:

`cloudflared tunnel run --token {{token}}`

- Run a tunnel using a specific credentials file:

`cloudflared tunnel run --credentials-file {{path/to/credentials.json}} {{tunnel_name}}`