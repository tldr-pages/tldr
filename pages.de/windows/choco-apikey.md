# choco apikey

> Verwalte die API-Schlüssel für die Quellen von Chocolatey.
> Weitere Informationen: <https://chocolatey.org/docs/commands-apikey>.

- Gib eine Liste von Quellen und ihren API-Schlüsseln aus:

`choco apikey`

- Zeige eine bestimmte Quelle und ihren API-Schlüssel an:

`choco apikey --source "{{quell_url}}"`

- Setze den API-Schlüssel für eine Quelle:

`choco apikey --source "{{quell_url}}" --key "{{api_schluessel}}"`

- Entferne den API-Schlüssel einer Quelle:

`choco apikey --source "{{quell_url}}" --remove`
