# tailscale

> The easiest and most secure way to use WireGuard and 2FA.
> More information: <https://tailscale.com>.

- Connect to Tailscale:

`sudo tailscale up`

- Disconnect from Tailscale:

`sudo tailscale down`

- Display current Tailscale IP addresses:

`tailscale ip`

- Ping a peer node at the Tailscale layer and display which route it took for each response:

`tailscale ping {{ip|hostname}}`

- Analyze the local network conditions and display the result:

`tailscale netcheck`

- Run a web server for controlling Tailscale:

`tailscale web`

- Display a shareable identifier to help diagnose issues:

`tailscale bugreport`

- Display help for a subcommand:

`tailscale {{subcommand}} --help`
