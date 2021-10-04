# apk

> Alpine Linux-Paketverwaltungstool.
> Weitere Informationen: <https://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management>.

- Aktualisiere die Indizes von allen externen Repositories:

`apk update`

- Installiere ein neues Paket:

`apk add {{paket}}`

- Entferne ein Paket:

`apk del {{paket}}`

- Repariere oder aktualisiere ein Paket, ohne die Hauptabhängigkeiten zu ändern:

`apk fix {{paket}}`

- Suche Pakete mit einem Schlüsselwort:

`apk search {{schlüsselwort}}`

- Erhalte Informationen über ein bestimmtes Paket:

`apk info {{paket}}`
