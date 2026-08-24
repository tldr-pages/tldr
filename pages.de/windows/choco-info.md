# choco info

> Zeige ausführliche Informationen über ein Chocolatey-Paket an.
> Weitere Informationen: <https://docs.chocolatey.org/en-us/choco/commands/info/>.

- Zeige Informationen über ein bestimmtes Paket an:

`choco info {{paket}}`

- Zeige Informationen über ein bestimmtes lokales Paket an:

`choco info {{paket}} {{[-l|--local-only]}}`

- Gib eine eigene Quelle an, von der Paket-Informationen abgerufen werden:

`choco info {{paket}} {{[-s|--source]}} {{quell_url|alias}}`

- Gib einen Benutzernamen und ein Passwort für die Authentifizierung an:

`choco info {{paket}} {{[-u|--user]}} {{benutzername}} {{[-p|--password]}} {{passwort}}`
