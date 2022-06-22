# warp-cli

> Official command-line client for Cloudflare's WARP service.
> More information: <https://developers.cloudflare.com/warp-client/>.

- Start WARP service if it is not already enabled:

`sudo systemctl start warp-svc`

- Register the current device to WARP (must be run before first connection):

`warp-cli register`

- Connect to WARP:

`warp-cli connect`

- Disconnect from WARP:

`warp-cli disconnect`

- Display the WARP connection status:

`warp-cli status`

- Display help:

`warp-cli help`

- Display help for a subcommand:

`warp-cli help {{subcommand}}`
