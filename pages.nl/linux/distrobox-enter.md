# distrobox-enter

> Betreed een distrobox container.
> Subcommando van `distrobox`. Bekijk ook: `tldr distrobox`.
> Standaard commando dat wordt uitgevoerd is je SHELL, maar je kan verschillende shells of hele commando's specificeren. Indien gebruikt in een script/applicatie/service, kunt u de `--headless`-modus gebruiken om de tty en interactiviteit uit te schakelen.
> Meer informatie: <https://distrobox.it/usage/distrobox-enter>.

- Betreed een distrobox container:

`distrobox-enter {{container_name}}`

- Betreed een distrobox container en voer een commando uit bij het inloggen:

`distrobox-enter {{container_name}} -- {{sh -l}}`

- Betreed een distrobox container zonder een tty the instanteren:

`distrobox-enter --name {{container_name}} -- {{uptime -p}}`
