# warp-cli

> Connect, disconnect, and switch modes of a connection to Cloudflare's WARP service.
> WARP is a VPN that encrypts traffic for privacy, security, and speed.
> See also: `fastd`, `ivpn`, `mozillavpn`, `mullvad`.
> More information: <https://developers.cloudflare.com/warp-client/>.

- Register the current device to WARP (must be run before first connection):

`warp-cli registration new`

- Display the current registration information:

`warp-cli registration show`

- Connect to WARP:

`warp-cli connect`

- Disconnect from WARP:

`warp-cli disconnect`

- Display the WARP connection status:

`warp-cli status`

- Display current application settings:

`warp-cli settings list`

- Switch to a specific mode:

`warp-cli mode {{warp|doh|warp+doh|dot|warp+dot|proxy|tunnel_only}}`
