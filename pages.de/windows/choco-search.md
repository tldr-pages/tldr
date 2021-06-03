# choco search

> Suche mit Chocolatey nach einem lokal oder im Internet verfügbaren Paket.
> Weitere Informationen: <https://chocolatey.org/docs/commands-search>.

- Suche nach einem Paket:

`choco search {{suchabfrage}}`

- Suche nur lokal nach einem Paket:

`choco search {{suchabfrage}} --local-only`

- Suche nur nach genauen Übereinstimmungen:

`choco search {{suchabfrage}} --exact`

- Stimme allen Fragen automatisch zu:

`choco search {{suchabfrage}} --yes`

- Gib eine eigene Quelle an, welche nach Paketen durchsucht wird:

`choco search {{suchabfrage}} --source {{quell_url|alias}}`

- Gib einen Benutzernamen und ein Passwort für die Authentifizierung an:

`choco search {{suchabfrage}} --user {{benutzername}} --password {{passwort}}`
