# frpc

> Maak verbinding met een `frps`-server om verbindingen op de huidige host te proxyen.
> Onderdeel van `frp`.
> Meer informatie: <https://github.com/fatedier/frp>.

- Start de service met het standaardconfiguratiebestand (aangenomen wordt dat dit `frps.ini` is in de huidige map):

`frpc`

- Start de service met het nieuwere TOML-configuratiebestand:

`frpc {{[-c|--config]}} {{pad/naar/frps.toml}}`

- Start de service met een specifiek configuratiebestand:

`frpc {{[-c|--config]}} {{pad/naar/bestand}}`

- Controleer of het configuratiebestand geldig is:

`frpc verify {{[-c|--config]}} {{pad/naar/bestand}}`

- Toon het script om autocompletion op te zetten voor Bash, fish, PowerShell of Zsh:

`frpc completion {{bash|fish|powershell|zsh}}`

- Toon de versie:

`frpc {{[-v|--version]}}`
