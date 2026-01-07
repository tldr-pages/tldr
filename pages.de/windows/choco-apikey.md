# choco apikey

> Verwalte die API-Schlüssel für die Quellen von Chocolatey.
> Weitere Informationen: <https://docs.chocolatey.org/en-us/create/commands/api-key/>.

- Gib eine Liste von Quellen und ihren API-Schlüsseln aus:

`choco apikey`

- Zeige eine bestimmte Quelle und ihren API-Schlüssel an:

`choco apikey {{[-s|--source]}} "{{quell_url}}"`

- Setze den API-Schlüssel für eine Quelle:

`choco apikey {{[-s|--source]}} "{{quell_url}}" {{[-k|--api-key]}} "{{api_schluessel}}"`

- Entferne den API-Schlüssel einer Quelle:

`choco apikey {{[-s|--source]}} "{{quell_url}}" --remove`
