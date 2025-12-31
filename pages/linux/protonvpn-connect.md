# protonvpn connect

> Connect to ProtonVPN.
> More information: <https://github.com/Rafficer/linux-cli-community>.

- Connect to ProtonVPN interactively:

`protonvpn {{[c|connect]}}`

- Connect to ProtonVPN using the fastest server available:

`protonvpn {{[c|connect]}} {{[-f|--fastest]}}`

- Connect to ProtonVPN using a specific server with a specific protocol:

`protonvpn {{[c|connect]}} {{server_name}} -p {{udp|tcp}}`

- Connect to ProtonVPN using a random server with a specific protocol:

`protonvpn {{[c|connect]}} {{[-r|--random]}} -p {{udp|tcp}}`

- Connect to ProtonVPN using the fastest Tor-supporting server:

`protonvpn {{[c|connect]}} --tor`

- Display help:

`protonvpn {{[c|connect]}} --help`
