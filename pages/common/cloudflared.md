# cloudflared

> Command line tool to create a persistent connection to the Cloudflare network
> More information: <https://developers.cloudflare.com/argo-tunnel/>.

- Authenticate and associate the connection to a domain in the Cloudflare account:

`cloudflared tunnel login`

- Establish a tunnel between the local server to a host in Cloudflare:

`cloudflared tunnel --hostname {{hostname}} localhost:{{port_number}} --no-tls-verify`

- Save logs to a file:

`cloudflared tunnel --hostname {{hostname}} http://localhost:{{port_number}} --loglevel {{panic|fatal|error|warn|info|debug}} --logfile {{path/to/file}}`

- Install cloudflared as a system service:

`cloudflared service install`