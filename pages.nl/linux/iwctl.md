# iwctl

> Beheer de `iwd` netwerk supplicant.
> Meer informatie: <https://manned.org/iwctl>.

- Start de interactieve modus, in deze modus kunt u de commando's direct invoeren, met autocompletion:

`iwctl`

- Toon jouw Wi-Fi-stations:

`iwctl station list`

- Begin met zoeken naar netwerken met een station:

`iwctl station {{station}} scan`

- Toon de netwerken die zijn gevonden door het station:

`iwctl station {{station}} get-networks`

- Verbind met een netwerk met een station, als er inloggegevens nodig zijn, worden deze opgevraagd:

`iwctl station {{station}} connect {{netwerk_naam}}`

- Toon de help:

`iwctl {{[-h|--help]}}`
