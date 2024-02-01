# cloudflared

> Command-line tool to create a persistent connection to the Cloudflare network.
> More information: <https://developers.cloudflare.com/argo-tunnel/>.

- Authenticate and associate the connection to a domain in the Cloudflare account:

`cloudflared tunnel login`

- Create a tunnel with a specific name:

`cloudflared tunnel create {{name}}`

- Establish a tunnel to a host in Cloudflare from the local server:

`cloudflared tunnel --hostname {{hostname}} localhost:{{port_number}}`

- Establish a tunnel to a host in Cloudflare from the local server, without verifying the local server's certificate:

`cloudflared tunnel --hostname {{hostname}} localhost:{{port_number}} --no-tls-verify`

- Save logs to a file:

`cloudflared tunnel --hostname {{hostname}} http://localhost:{{port_number}} --loglevel {{panic|fatal|error|warn|info|debug}} --logfile {{path/to/file}}`

- Install cloudflared as a system service:

`cloudflared service install`
