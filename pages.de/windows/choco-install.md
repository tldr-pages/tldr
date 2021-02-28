# choco install

> Installiere ein oder mehrere Pakete mit Chocolatey.
> Mehr Informationen: <https://chocolatey.org/docs/commands-install>.

- Installiere ein oder mehrere Pakete, deren Namen mit Leerzeichen getrennt sind:

`choco install {{paket(e)}}`

- Installiere Pakete aus einer Konfigurationsdatei:

`choco install {{pfad/zur/pakete.config}}`

- Installiere Pakete aus einer `nuspec`- oder `nupkg`-Datei:

`choco install {{pfad/zur/datei}}`

- Installiere eine bestimmte Version eines Pakets:

`choco install {{paket}} --version {{version}}`

- Erlaube die gleichzeitige Installation mehrerer Versionen eines Pakets:

`choco install {{paket}} --allow-multiple`

- Stimme allen Fragen automatisch zu:

`choco install {{paket}} --yes`

- Gib eine eigene Quelle an, von der Paket-Informationen abgerufen werden:

`choco install {{paket}} --source {{quell_url|alias}}`

- Gib einen Benutzernamen und ein Passwort für die Authentifizierung an:

`choco install {{paket}} --user {{benutzername}} --password {{passwort}}`
