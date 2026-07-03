# cloudflared tunnel route dns

> Route a hostname to a tunnel by creating a DNS CNAME record.
> See also: `cloudflared tunnel route`.
> More information: <https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/>.

- Create a DNS record pointing a hostname to a tunnel:

`cloudflared tunnel route dns {{tunnel_name}} {{hostname.example.com}}`

- Overwrite an existing DNS record with the same hostname:

`cloudflared tunnel route dns {{[-f|--overwrite-dns]}} {{tunnel_name}} {{hostname.example.com}}`