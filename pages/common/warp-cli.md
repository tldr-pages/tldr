# warp-cli

> Connect, disconnect and switch modes of a connection to Cloudflare's WARP service.
> WARP is a VPN that encrypts traffic for privacy, security, and speed.
> See also: `fastd`, `ivpn`, `mozzilavpn`, `mullvad`.
> More information: <https://developers.cloudflare.com/warp-client/>.

- Register the current device to WARP (must be run before first connection):

`warp-cli register`

- Connect to WARP:

`warp-cli connect`

- Disconnect from WARP:

`warp-cli disconnect`

- Display the WARP connection status:

`warp-cli status`

- Switch to a specific mode:

`warp-cli set-mode {{mode}}`

- Display help:

`warp-cli help`

- Display help for a subcommand:

`warp-cli help {{subcommand}}`
