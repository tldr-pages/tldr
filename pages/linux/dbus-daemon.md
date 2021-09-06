# dbus-daemon

> The D-Bus message daemon, allowing multiple programs to exchange messages.
> More information: <https://www.freedesktop.org/wiki/Software/dbus/>.

- Run the daemon with a configuration file:

`dbus-daemon --config-file {{path/to/file}}`

- Run the daemon with the standard per-login-session message bus configuration:

`dbus-daemon --session`

- Run the daemon with the standard systemwide message bus configuration:

`dbus-daemon --system`

- Set the address to listen on and override the configuration value for it:

`dbus-daemon --address {{address}}`

- Output the process ID to stdout:

`dbus-daemon --print-pid`

- Force the message bus to write to the system log for messages:

`dbus-daemon --syslog`
