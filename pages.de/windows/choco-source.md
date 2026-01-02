# choco source

> Verwalte die Paketquellen mit Chocolatey.
> Weitere Informationen: <https://docs.chocolatey.org/en-us/choco/commands/source/>.

- Gib alle momentan verfügbaren Quellen aus:

`choco source list`

- Füge eine neue Paketquelle hinzu:

`choco source add {{[-n|--name]}} {{name}} {{[-s|--source]}} {{url}}`

- Füge eine neue Paketquelle mit Zugangsdaten hinzu:

`choco source add {{[-n|--name]}} {{name}} {{[-s|--source]}} {{url}} {{[-u|--user]}} {{benutzername}} {{[-p|--password]}} {{passwort}}`

- Füge eine neue Paketquelle mit Client-Zertifikat hinzu:

`choco source add {{[-n|--name]}} {{name}} {{[-s|--source]}} {{url}} --cert {{pfad/zu/zertifikat}}`

- Aktiviere eine Paketquelle:

`choco source enable {{[-n|--name]}} {{name}}`

- Deaktiviere eine Paketquelle:

`choco source disable {{[-n|--name]}} {{name}}`

- Entferne eine Paketquelle:

`choco source remove {{[-n|--name]}} {{name}}`
