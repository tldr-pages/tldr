# systemd-stdio-bridge

> Implement a proxy between `stdin`/`stdout` and a D-Bus.
> Note: It expects to receive an open connection via `stdin`/`stdout` when started, and will create a new connection to the specified bus.
> More information: <https://www.freedesktop.org/software/systemd/man/latest/systemd-stdio-bridge.html>.

- Forward `stdin`/`stdout` to the local system bus:

`systemd-stdio-bridge`

- Forward `stdin`/`stdout` to a specific user's D-Bus:

`systemd-stdio-bridge --{{user}}`

- Forward `stdin`/`stdout` to the local system bus within a specific container:

`systemd-stdio-bridge --machine={{mycontainer}}`

- Forward `stdin`/`stdout` to a custom D-Bus address:

`systemd-stdio-bridge --bus-path=unix:path={{/custom/dbus/socket}}`
