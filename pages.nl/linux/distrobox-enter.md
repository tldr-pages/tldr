# distrobox-enter

> Betreed een Distrobox container. Bekijk ook: `tldr distrobox`.
> Standaard commando dat wordt uitgevoerd is je SHELL, maar je kan verschillende shells of hele commando's specificeren. Indien gebruikt in een script/applicatie/service, kunt u de `--headless`-modus gebruiken om de tty en interactiviteit uit te schakelen.
> Meer informatie: <https://distrobox.it/usage/distrobox-enter>.

- Betreed een Distrobox container:

`distrobox-enter {{container_name}}`

- Betreed een Distrobox container en voer een commando uit bij het inloggen:

`distrobox-enter {{container_name}} -- {{sh -l}}`

- Betreed een Distrobox container zonder een tty the instanteren:

`distrobox-enter --name {{container_name}} -- {{uptime -p}}`
