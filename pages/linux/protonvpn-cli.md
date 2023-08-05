# protonvpn-cli

> Official ProtonVPN client.
> More information: <https://github.com/ProtonVPN/linux-cli>.

- Log in to the ProtonVPN account:

`protonvpn-cli login {{username}}`

- Start a kill switch upon connecting to ProtonVPN:

`protonvpn-cli killswitch --on`

- Connect to ProtonVPN interactively:

`protonvpn-cli connect`

- Display connection status:

`protonvpn-cli status`

- Block malware using ProtonVPN NetShield:

`protonvpn-cli netshield --malware`

- Disconnect from ProtonVPN:

`protonvpn-cli disconnect`

- Display the current ProtonVPN configuration:

`protonvpn-cli config --list`

- Display help for a subcommand:

`protonvpn-cli {{subcommand}} --help`
