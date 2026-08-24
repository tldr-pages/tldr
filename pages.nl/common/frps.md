# frps

> Stel snel een reverse proxy-service in.
> Onderdeel van `frp`.
> Meer informatie: <https://github.com/fatedier/frp>.

- Start de service met het standaardconfiguratiebestand (aangenomen wordt dat dit `frps.ini` is in de huidige map):

`frps`

- Start de service met het nieuwere TOML-configuratiebestand:

`frps {{[-c|--config]}} {{pad/naar/frps.toml}}`

- Start de service met een specifiek configuratiebestand:

`frps {{[-c|--config]}} {{pad/naar/bestand}}`

- Controleer of het configuratiebestand geldig is:

`frps verify {{[-c|--config]}} {{pad/naar/bestand}}`

- Toon het script om autocompletion op te zetten voor Bash, fish, PowerShell of Zsh:

`frps completion {{bash|fish|powershell|zsh}}`

- Toon de versie:

`frps {{[-v|--version]}}`
