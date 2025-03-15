# tailscale

> A private WireGuard network service.
> Some subcommands such as `up` have their own usage documentation.
> More information: <https://tailscale.com/kb/1080/cli>.

- Allow the current user to operate on the Tailscale daemon:

`sudo tailscale set --operator $USER`

- Connect to Tailscale:

`tailscale up`

- Disconnect from Tailscale:

`tailscale down`

- Display all devices connected to Tailscale (with their IP addresses):

`tailscale status`

- Ping a peer node at the Tailscale layer and display which route it took for each response:

`tailscale ping {{ip|hostname}}`

- Analyze the local network conditions and display the result:

`tailscale netcheck`

- Start a web server for controlling the Tailscale daemon:

`tailscale web`

- Display a shareable identifier to help diagnose issues:

`tailscale bugreport`
