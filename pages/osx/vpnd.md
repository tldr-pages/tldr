# vpnd

> Listens for incoming VPN connections.
> It should not be invoked manually.

- Start the daemon:

`vpnd`

- Run the daemon in the foreground:

`vpn -x`

- Run the daemon in the foreground and print logs to the terminal:

`vpnd -d`

- Run the daemon in the foreground, print logs to the terminal, and quit after validating arguments:

`vpn -n`

- Print usage summary and exit:

`vpn -h`

- Run the daemon for a specific server configuration:

`vpn -i {{server_id}}`
