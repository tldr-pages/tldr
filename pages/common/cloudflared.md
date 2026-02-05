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

- Save logs to a file:

`cloudflared tunnel --loglevel {{panic|fatal|error|warn|info|debug}} --logfile {{path/to/file}} run {{name}}`

- Run a named tunnel (reads configuration from `config.yml`):

`cloudflared tunnel run {{name}}`

- Start a temporary tunnel to expose a local service (no account required):

`cloudflared tunnel --url http://localhost:{{port}}`

- Install cloudflared as a system service:

`cloudflared service install`
