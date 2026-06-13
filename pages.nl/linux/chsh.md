# chsh

> Verander de login shell van een gebruiker.
> Onderdeel van `util-linux`.
> Meer informatie: <https://manned.org/chsh>.

- Stel een specifieke login shell interactief in voor de huidige gebruiker:

`chsh`

- Toon beschikbare shells:

`chsh {{[-l|--list-shells]}}`

- Stel een specifieke login shell in voor de huidige gebruiker:

`chsh {{[-s|--shell]}} {{pad/naar/shell}}`

- Stel een login shell in voor een specifieke gebruiker:

`sudo chsh {{[-s|--shell]}} {{pad/naar/shell}} {{gebruikersnaam}}`
