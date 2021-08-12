# swupd

> Utilitar de gestionare pachet pentru Clear Linux.
> Mai multe informaţii: <https://docs.01.org/clearlinux/latest/guides/clear/swupd.html>

- Actualizare la cea mai recentă versiune:

`sudo swupd update`

- Afișați versiunea curentă și verificați dacă există una mai nouă:

`swupd check-update`

- Lista pachetelor instalate:

`swupd bundle-list`

- Localizați pachetul unde există un pachet dorit:

`swupd search -b {{package}}`

- Instalați un pachet nou:

`sudo swupd bundle-add {{bundle}}`

- Scoateți un pachet:

`sudo swupd bundle-remove {{bundle}}`

- Corectați fișierele rupte sau lipsă:

`sudo swupd verify`
