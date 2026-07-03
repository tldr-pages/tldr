# cloudflared access ssh-config

> Print an example SSH configuration for connecting to a Cloudflare Access protected host.
> See also: `cloudflared access ssh`, `cloudflared access ssh-gen`.
> More information: <https://developers.cloudflare.com/cloudflare-one/>.

- Print an example configuration for a protected host:

`cloudflared access ssh-config --hostname {{ssh.example.com}}`

- Print a configuration that uses short-lived certificates:

`cloudflared access ssh-config --hostname {{ssh.example.com}} --short-lived-cert`