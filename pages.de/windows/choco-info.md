# choco info

> Zeige ausführliche Informationen über ein Chocolatey-Paket an.
> Mehr Informationen: <https://chocolatey.org/docs/commands-info>.

- Zeige Informationen über ein bestimmtes Paket an:

`choco info {{paket}}`

- Zeige Informationen über ein bestimmtes lokales Paket an:

`choco info {{paket}} --local-only`

- Gib eine eigene Quelle an, von der Paket-Informationen abgerufen werden:

`choco info {{paket}} --source {{quell_url|alias}}`

- Gib einen Benutzernamen und ein Passwort für die Authentifizierung an:

`choco info {{paket}} --user {{benutzername}} --password {{passwort}}`
