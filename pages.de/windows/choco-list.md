# choco list

> Zeige mit Chocolatey eine Liste von Paketen an.
> Weitere Informationen: <https://chocolatey.org/docs/commands-list>.

- Zeige alle verfügbaren Pakete an:

`choco list`

- Zeige alle lokal installierten Pakete an:

`choco list --local-only`

- Zeige eine Liste einschließlich der lokalen Windows-Programme an:

`choco list --include-programs`

- Zeige nur zugelassene Pakete an:

`choco list --approved-only`

- Gib eine eigene Quelle an, von der Paket-Informationen abgerufen werden:

`choco list --source {{quell_url|alias}}`

- Gib einen Benutzernamen und ein Passwort für die Authentifizierung an:

`choco list --user {{benutzername}} --password {{passwort}}`
