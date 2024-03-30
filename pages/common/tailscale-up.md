# tailscale up

> Connect the client to the Tailscale network.
> In version 1.8 and above, command-line arguments are stored and reused until they're overwritten or `--reset` is called.
> More information: <https://tailscale.com/kb/1080/cli/#up>.

- Connect to Tailscale:

`sudo tailscale up`

- Connect and offer the current machine to be an exit node for internet traffic:

`sudo tailscale up --advertise-exit-node`

- Connect using a specific node for internet traffic:

`sudo tailscale up --exit-node={{exit_node_ip}}`

- Connect and block incoming connections to the current node:

`sudo tailscale up --shields-up`

- Connect and don't accept DNS configuration from the admin panel (defaults to `true`):

`sudo tailscale up --accept-dns=false`

- Connect and configure Tailscale as a subnet router:

`sudo tailscale up --advertise-routes={{10.0.0.0/24,10.0.1.0/24,...}}`

- Connect and accept subnet routes from Tailscale:

`sudo tailscale up --accept-routes`

- Reset unspecified settings to their default values and connect:

`sudo tailscale up --reset`
