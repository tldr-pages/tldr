# apk

> Alpine Linux-Paketverwaltungstool.
> Weitere Informationen: <https://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management>.

- Aktualisiere die Indexe von allen externen Repositories:

`apk update`

- Installiere ein neues Paket:

`apk add {{paket}}`

- Entferne ein Paket:

`apk del {{paket}}`

- Reparieren Sie das Paket oder aktualisieren es, ohne die Hauptabhängigkeiten zu ändern:

`apk fix {{paket}}`

- Suche Pakete mit einem Schlüsselwort:

`apk search {{schlüsselwort}}`

- Bekomme Informationen von einem spezifischen Paket:

`apk info {{paket}}`
