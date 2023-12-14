# cupsctl

> Update or query a server's cupsd.conf.
> More information: <https://www.cups.org/doc/man-cupsctl.html>.

- Display current configuration values:

`cupsctl`

- Display the configuration values of a specific server:

`cupsctl -h {{server[:port]}}`

- Display current configuration values [E]ncrypting the connection to the scheduler:

`cupsctl -E`

- Enable or disable debug logging to the error_log file:

`cupsctl --debug-logging|--no-debug-loging`

- Enable or disable remote administration:

`cupsctl --remote-admin|--no-remote-admin`

- Parse the current debug logging state:

`cupsctl | grep '^_debug_logging' | awk -F= '{print $2}'`
