# cloudflared

> Create a persistent connection to the Cloudflare network.
> More information: <https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/>.

- Authenticate and associate the connection to a domain in the Cloudflare account:

`cloudflared tunnel login`

- Create a tunnel with a specific name:

`cloudflared tunnel create {{name}}`

- List all tunnels in the account:

`cloudflared tunnel list`

- Create a DNS CNAME record pointing to a tunnel:

`cloudflared tunnel route dns {{name|uuid}} {{hostname}}`

- Run a tunnel and proxy traffic to a local service:

`cloudflared tunnel run --url http://localhost:{{port}} {{name}}`

- Start a temporary tunnel to expose a local service (no account required):

`cloudflared tunnel --url http://localhost:{{port}}`

- Delete a tunnel:

`cloudflared tunnel delete {{name|uuid}}`

- Install cloudflared as a system service:

`cloudflared service install`
