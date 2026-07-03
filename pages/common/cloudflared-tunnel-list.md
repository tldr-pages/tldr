# cloudflared tunnel list

> List the tunnels in your Cloudflare account.
> See also: `cloudflared tunnel info`.
> More information: <https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/>.

- List all tunnels:

`cloudflared tunnel list`

- Include deleted tunnels in the list:

`cloudflared tunnel list {{[-d|--show-deleted]}}`

- Filter by tunnel name:

`cloudflared tunnel list {{[-n|--name]}} {{tunnel_name}}`

- Sort by a specific field:

`cloudflared tunnel list --sort-by {{name|id|createdAt|deletedAt|numConnections}}`

- Output as JSON:

`cloudflared tunnel list {{[-o|--output]}} json`