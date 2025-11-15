# tailscale up

> Connect the client to the Tailscale network.
> Note: Run `sudo tailscale set --operator $USER` to allow the current user to run these commands.
> All options described here can be changed later using `tailscale set --option argument`. Use `--option=false` to disable options that don't require arguments.
> More information: <https://tailscale.com/kb/1080/cli/#up>.

- Connect to Tailscale:

`tailscale up`

- Connect and offer the current machine to be an exit node for internet traffic:

`tailscale up --advertise-exit-node`

- Connect using a specific node for internet traffic:

`tailscale up --exit-node {{exit_node_ip}}`

- Connect and block incoming connections to the current node:

`tailscale up --shields-up`

- Connect and don't accept DNS configuration from the admin panel (defaults to `true`):

`tailscale up --accept-dns=false`

- Connect and configure Tailscale as a subnet router:

`tailscale up --advertise-routes {{10.0.0.0/24,10.0.1.0/24,...}}`

- Connect and accept subnet routes from Tailscale:

`tailscale up --accept-routes`

- Reset unspecified settings to their default values and connect:

`tailscale up --reset`
