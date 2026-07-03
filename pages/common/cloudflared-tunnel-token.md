# cloudflared tunnel token

> Fetch the credentials token used to run an existing tunnel.
> See also: `cloudflared tunnel run`.
> More information: <https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/>.

- Print the token for a tunnel by name or UUID:

`cloudflared tunnel token {{tunnel_name}}`

- Write the token to a credentials file:

`cloudflared tunnel token --cred-file {{path/to/credentials.json}} {{tunnel_name}}`