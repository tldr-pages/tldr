# cupsctl

> Update or query a server's `cupsd.conf`.
> More information: <https://openprinting.github.io/cups/doc/man-cupsctl.html>.

- Display the current configuration values:

`cupsctl`

- Display the configuration values of a specific server:

`cupsctl -h {{server[:port]}}`

- Enable encryption on the connection to the scheduler:

`cupsctl -E`

- Enable or disable debug logging to the `error_log` file:

`cupsctl {{--debug-logging|--no-debug-logging}}`

- Enable or disable remote administration:

`cupsctl {{--remote-admin|--no-remote-admin}}`

- Parse the current debug logging state:

`cupsctl | grep '^_debug_logging' | awk -F= '{print $2}'`
