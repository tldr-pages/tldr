# cloudflared access ssh

> Proxy SSH traffic to a Cloudflare Access protected host over the Cloudflare edge.
> See also: `cloudflared access rdp`, `cloudflared access ssh-config`.
> More information: <https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/>.

- Proxy SSH traffic to a protected host:

`cloudflared access ssh --hostname {{ssh.example.com}}`

- Forward the connection to a local listener (for use as an SSH `ProxyCommand`):

`cloudflared access ssh --hostname {{ssh.example.com}} --url {{localhost:1234}}`

- Authenticate using an Access service token:

`cloudflared access ssh --hostname {{ssh.example.com}} --service-token-id {{id}} --service-token-secret {{secret}}`
