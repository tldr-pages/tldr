# krdc

> Connect to a remote desktop server.
> More information: <https://invent.kde.org/network/krdc#usage>.

- Start KRDC:

`krdc`

- Automatically connect to a host with the current username using VNC

`krdc {{remote_host}}`

- Specify the protocol and username used to connect to a host:

`krdc {{vnc|rdp}}://{{username}}@{{remote_host}}`

- Start the connection in fullscreen mode:

`krdc {{rdp://username@ip_address}} --fullscreen`
