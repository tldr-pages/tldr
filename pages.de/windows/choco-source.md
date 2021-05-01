# choco source

> Verwalte die Paketquellen mit Chocolatey.
> Weitere Informationen: <https://chocolatey.org/docs/commands-source>.

- Gib alle momentan verfügbaren Quellen aus:

`choco source list`

- Füge eine neue Paketquelle hinzu:

`choco source add --name {{name}} --source {{url}}`

- Füge eine neue Paketquelle mit Zugangsdaten hinzu:

`choco source add --name {{name}} --source {{url}} --user {{benutzername}} --password {{passwort}}`

- Füge eine neue Paketquelle mit Client-Zertifikat hinzu:

`choco source add --name {{name}} --source {{url}} --cert {{pfad/zu/zertifikat}}`

- Aktiviere eine Paketquelle:

`choco source enable --name {{name}}`

- Deaktiviere eine Paketquelle:

`choco source disable --name {{name}}`

- Entferne eine Paketquelle:

`choco source remove --name {{name}}`
