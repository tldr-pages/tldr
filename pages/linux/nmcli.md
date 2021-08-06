# nmcli

> A command-line tool for controlling NetworkManager.
> For in-depth commands, see `nmcli-{{command}}`.
> More information: <https://manned.org/nmcli>.

- Run an `nmcli` subcommand:

`nmcli {{agent|connection|device|general|help|monitor|networking|radio}} {{command_options}}`

- Display the current version of NetworkManager:

`nmcli --version`

- Display help:

`nmcli --help`

- Display help for a subcommand:

`nmcli {{subcommand}} --help`

- Displays a table of available wifi access points:

`nmcli dev wifi`

- Connect to a WiFi network:

`nmcli device wifi connect {{SSID}} password {{PASSWORD}}`

