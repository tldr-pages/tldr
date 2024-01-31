# vpnd

> Listens for incoming VPN connections.
> It should not be invoked manually.
> More information: <https://keith.github.io/xcode-man-pages/vpnd.8.html>.

- Start the daemon:

`vpnd`

- Run the daemon in the foreground:

`vpnd -x`

- Run the daemon in the foreground and print logs to the terminal:

`vpnd -d`

- Run the daemon in the foreground, print logs to the terminal, and quit after validating arguments:

`vpnd -n`

- Run the daemon for a specific server configuration:

`vpnd -i {{server_id}}`

- Display help:

`vpnd -h`
