# dpkg

> Debian Paketmanager.
> Manche Unterbefehle wie `dpkg deb` sind separat dokumentiert.
> Weitere Informationen: <https://manpages.debian.org/latest/dpkg/dpkg.html>.

- Installiere ein Paket:

`dpkg -i {{pfad/zu/datei.deb}}`

- Entferne ein Paket:

`dpkg -r {{paketname}}`

- Liste installierte Pakete auf:

`dpkg -l {{muster}}`

- Liste die Inhalte eines Pakets auf:

`dpkg -L {{paketname}}`

- Liste die Inhalte einer lokalen Paketdatei auf:

`dpkg -c {{pfad/zu/datei.deb}}`

- Finde heraus welche Pakete eine Datei besitzen:

`dpkg -S {{dateiname}}`
