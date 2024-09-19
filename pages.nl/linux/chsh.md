# chsh

> Verander de login shell van een gebruiker.
> Onderdeel van `util-linux`.
> Meer informatie: <https://manned.org/chsh>.

- Stel een specifieke login shell interactief in voor de huidige gebruiker:

`chsh`

- Stel een specifieke login[s]hell in voor de huidige gebruiker:

`chsh --shell {{pad/naar/shell}}`

- Stel een login[s]hell in voor een specifieke gebruiker:

`sudo chsh --shell {{pad/naar/shell}} {{gebruikersnaam}}`

- Toon ([l]) beschikbare shells:

`chsh --list-shells`
