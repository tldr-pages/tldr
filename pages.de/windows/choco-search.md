# choco search

> Suche mit Chocolatey nach einem lokal oder im Internet verfügbaren Paket.
> Weitere Informationen: <https://docs.chocolatey.org/en-us/choco/commands/search/>.

- Suche nach einem Paket:

`choco search {{suchabfrage}}`

- Suche nur lokal nach einem Paket:

`choco search {{suchabfrage}} --local-only`

- Suche nur nach genauen Übereinstimmungen:

`choco search {{suchabfrage}} {{[-e|--exact]}}`

- Stimme allen Fragen automatisch zu:

`choco search {{suchabfrage}} {{[-y|--yes]}}`

- Gib eine eigene Quelle an, welche nach Paketen durchsucht wird:

`choco search {{suchabfrage}} {{[-s|--source]}} {{quell_url|alias}}`

- Gib einen Benutzernamen und ein Passwort für die Authentifizierung an:

`choco search {{suchabfrage}} {{[-u|--user]}} {{benutzername}} {{[-p|--password]}} {{passwort}}`
