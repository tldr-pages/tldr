# cloudflared tail

> Stream logs from a remote cloudflared instance.
> More information: <https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/>.

- Stream logs for a tunnel using its token:

`cloudflared tail --token {{token}}`

- Filter by event type:

`cloudflared tail --event {{cloudflared|http|tcp|udp}}`

- Filter by log level:

`cloudflared tail --level {{debug|info|warn|error}}`

- Target a specific connector when a tunnel has several:

`cloudflared tail --connector-id {{connector_id}}`

- Output logs as JSON:

`cloudflared tail --output json`