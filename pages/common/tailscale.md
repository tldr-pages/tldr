# tailscale

> A private WireGuard network service.
> Some subcommands such as `up` have their own usage documentation.
> More information: <https://tailscale.com/kb/1080/cli>.

- Allow the current user to operate on the Tailscale daemon:

`sudo tailscale set --operator $USER`

- Handle connection to Tailscale (connect, disconnect, check status):

`tailscale {{up|down|status}}`

- Offer the current machine to be an exit node for internet traffic:

`tailscale set --advertise-exit-node`

- Use a specific exit node for internet traffic:

`tailscale set --exit-node {{ip_address|hostname}}`

- Display all devices connected to Tailscale (with their IP addresses):

`tailscale ping {{ip_address|hostname}}`

- Analyze the local network conditions and display the result:

`tailscale netcheck`

- Start a web server for controlling the Tailscale daemon:

`tailscale web`

- Display a shareable identifier to help diagnose issues:

`tailscale bugreport`
