# choco upgrade

> Aktualisiere mit Chocolatey ein oder mehrere Pakete.
> Mehr Informationen: <https://chocolatey.org/docs/commands-upgrade>.

- Aktualisiere ein oder mehrere Pakete, deren Namen mit Leerzeichen getrennt sind:

`choco upgrade {{paket(e)}}`

- Aktualisiere auf eine bestimmte Version des Pakets:

`choco upgrade {{paket}} --version {{version}}`

- Aktualisiere alle Pakete:

`choco upgrade all`

- Aktualisiere alle außer den angegebenen, durch Kommas getrennten Paketen:

`choco upgrade all --except "{{paket(e)}}"`

- Stimme allen Fragen automatisch zu:

`choco upgrade {{paket}} --yes`

- Gib eine eigene Quelle an, von der Pakete aktualisiert werden:

`choco upgrade {{paket}} --source {{quell_url|alias}}`

- Gib einen Benutzernamen und ein Passwort für die Authentifizierung an:

`choco upgrade {{paket}} --user {{benutzername}} --password {{passwort}}`
