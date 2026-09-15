# tailcat

> WireGuard-encrypted tunnels using Tailscale's data plane, like netcat but encrypted.
> In the examples below, an `addrblob` is the connection token (`tcom...`) printed by a running `tailcat` server, used by clients to reach it.
> More information: <https://github.com/tailscale/tailcat#usage>.

- Start a server that accepts one connection and writes to `stdout` (no local port; clients connect via the printed addrblob):

`tailcat`

- Start a server that exposes specific local TCP ports (e.g. an existing service on 22/80/443) to clients via the tunnel:

`tailcat --serve={{22,80,443}}`

- Start a server as an exit node, routing client traffic through this host's network:

`tailcat --serve=exit-node`

- Start an auth-free SSH server (Linux/macOS):

`tailcat --serve=no-auth-ssh`

- Connect to a server with an addrblob on a specific port, sending `stdin` to it:

`cat {{path/to/file}} | tailcat {{addrblob}} {{port}}`

- Ping a server to test connectivity, waiting for a direct path:

`tailcat ping --until-direct {{addrblob}}`

- SSH into a remote machine (server must expose port 22):

`tailcat ssh {{addrblob}}`

- Generate a new server key and print its addrblob:

`tailcat genkey --force`
