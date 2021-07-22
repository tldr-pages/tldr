# protonvpn-cli connect

> Official client to connect to ProtonVPN from the command-line.
> More information: <https://github.com/ProtonVPN/linux-cli>.

- Connect to ProtonVPN selecting the the server interactively:

`protonvpn-cli connect`

- Connect to ProtonVPN using the fastest server available:

`protonvpn-cli connect --fastest`

- Connect to ProtonVPN using a specific server with a specific protocol:

`protonvpn-cli connect {{server_name}} --protocol {{udp|tcp}}`

- Connect to ProtonVPN using a random server and a specific protocol:

`protonvpn-cli connect --random --protocol {{udp|tcp}}`

- Connect to ProtonVPN using the fastest Tor server:

`protonvpn-cli connect --tor`

- Display help:

`protonvpn connect --help`
