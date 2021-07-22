# protonvpn-cli connect

> Official client to connect to ProtonVPN from the command-line.
> More information: <https://github.com/ProtonVPN/linux-cli>.

- Connect to ProtonVPN selecting the the server interactively:

`protonvpn-cli connect`

- Connect to ProtonVPN using the fastest server available:

`protonvpn-cli connect --fastest`

- Connect to ProtonVPN using a specific server with TCP:

`protonvpn-cli connect {{server_name}} --protocol {{tcp}}`

- Connect to ProtonVPN using a random server and UDP:

`protonvpn-cli connect --random --protocol {{tcp}}`

- Connect to ProtonVPN using the fastest Tor server:

`protonvpn-cli connect --tor`

- Display help:

`protonvpn connect --help`
