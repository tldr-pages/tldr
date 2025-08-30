# iwctl

> Beheer de `iwd` netwerk supplicant.
> Meer informatie: <https://manned.org/iwctl>.

- Voer `iwctl` uit in interactieve modus:

`iwctl`

- Toon Wi-Fi-stations:

`iwctl station list`

- Zoek naar netwerken met een station:

`iwctl station {{station}} scan`

- Toon de netwerken die zijn gevonden door het station:

`iwctl station {{station}} get-networks`

- Verbind met een netwerk met een station, als er inloggegevens nodig zijn, worden deze opgevraagd:

`iwctl station {{station}} connect {{netwerk_naam}}`

- Toon de help:

`iwctl {{[-h|--help]}}`
