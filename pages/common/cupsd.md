# cupsd

> Server daemon for the CUPS print server.
> More information: <https://openprinting.github.io/cups/doc/man-cupsd.html>.

- Start `cupsd` in the background, aka. as a daemon:

`cupsd`

- Start `cupsd` on the [f]oreground:

`cupsd -f`

- [l]aunch `cupsd` on-demand (commonly used by `launchd` or `systemd`):

`cupsd -l`

- Start `cupsd` using the specified `cupsd.conf` [c]onfiguration file:

`cupsd -c {{path/to/cupsd.conf}}`

- Start `cupsd` using the specified `cups-files.conf` configuration file:

`cupsd -s {{path/to/cups-files.conf}}`

- [t]est the `cupsd.conf` [c]onfiguration file for errors:

`cupsd -t -c {{path/to/cupsd.conf}}`

- [t]est the `cups-files.conf` configuration file for errors:

`cupsd -t -s {{path/to/cups-files.conf}}`

- Display [h]elp:

`cupsd -h`
