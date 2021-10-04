# dpkg

> Debian Paketmanager.
> Einige Unterbefehle wie `dpkg deb` haben ihre eigene Gebrauchsdokumentation.
> Weitere Informationen: <https://manpages.debian.org/buster/dpkg/dpkg.1.en.html>.

- Installiere ein Paket:

`dpkg -i {{pfad/zur/datei.deb}}`

- Entferne ein Paket:

`dpkg -r {{paket_name}}`

- Liste installierte Pakete auf:

`dpkg -l {{muster}}`

- Liste die Inhalte eines Pakets auf:

`dpkg -L {{paket_name}}`

- Liste die Inhalte einer lokalen Paketdatei auf:

`dpkg -c {{pfad/zur/datei.deb}}`

- FInde heraus welche Pakete eine Datei besitzen:

`dpkg -S {{dateiname}}`
