# nmcli

> Manage the network configuration using NetworkManager.
> Some subcommands such as `nmcli monitor` have their own usage documentation.
> More information: <https://networkmanager.dev/docs/api/latest/nmcli.html>.

- List all available wifi networks:

`nmcli device wifi`

- Connect to a wifi network:

`nmcli dev wifi connect {{SSID}}`

- Run an `nmcli` subcommand:

`nmcli {{agent|connection|device|general|help|monitor|networking|radio}} {{command_options}}`

- Display the current version of NetworkManager:

`nmcli --version`

- Display help:

`nmcli --help`

- Display help for a subcommand:

`nmcli {{subcommand}} --help`
