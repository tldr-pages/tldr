# cloudflared access rdp

> Proxy RDP traffic to a Cloudflare Access protected host over the Cloudflare edge.
> See also: `cloudflared access ssh`.
> More information: <https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/>.

- Proxy RDP traffic to a protected host through a local listener:

`cloudflared access rdp --hostname {{rdp.example.com}} --url {{localhost:3389}}`

- Authenticate using an Access service token:

`cloudflared access rdp --hostname {{rdp.example.com}} --url {{localhost:3389}} --service-token-id {{id}} --service-token-secret {{secret}}`
