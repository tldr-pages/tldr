# choco outdated

> Überprüfe mit Chocolatey, ob Pakete veraltet sind.
> Mehr Informationen: <https://chocolatey.org/docs/commands-outdated>.

- Zeige eine Liste von veralteten Paketen im Tabellen-Format:

`choco outdated`

- Ignoriere angeheftete Pakete in der Ausgabe:

`choco outdated --ignore-pinned`

- Gib eine eigene Quelle an, mit der die Aktualität der Pakete überprüft wird:

`choco outdated --source {{source_url|alias}}`

- Gib einen Benutzernamen und ein Passwort für die Authentifizierung an:

`choco outdated --user {{benutzername}} --password {{passwort}}`
