# apk

> Apline Linux Paket Management Tool.
> Mehr Informationen: <https://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management>.

- Update die Repository Indizes aller Remote Repositories:

`apk update`

- Installiere ein neues Paket:

`apk add {{paket}}`

- Entferne ein Paket:

`apk del {{paket}}`

- Repariere ein Paket oder upgrade es ohne die Hauptabhängigkeiten zu verändern:

`apk fix {{paket}}`

- Suche ein paket nach Stichwort:

`apk search {{keyword}}`

- Bekomme Informationen über ein spezifisches Paket:

`apk info {{package}}`
