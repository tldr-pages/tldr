# cloudflared tunnel

> Create and manage Cloudflare Tunnels to expose local services to the Internet.
> See also: `cloudflared tunnel create`, `cloudflared tunnel run`, `cloudflared tunnel route`.
> More information: <https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/>.

- Authenticate cloudflared with your Cloudflare account:

`cloudflared tunnel login`

- Create a named tunnel:

`cloudflared tunnel create {{tunnel_name}}`

- List existing tunnels:

`cloudflared tunnel list`

- Route a DNS hostname to a tunnel:

`cloudflared tunnel route dns {{tunnel_name}} {{hostname.example.com}}`

- Run a named tunnel:

`cloudflared tunnel run {{tunnel_name}}`

- Start a temporary tunnel exposing a local service (no account required):

`cloudflared tunnel --url http://localhost:{{8000}}`

- Delete a tunnel:

`cloudflared tunnel delete {{tunnel_name}}`
