# a2query

> Zeigt Apache Laufzeitkonfigurationen auf Debian-basierten Betriebssystemen an.
> Weitere Informationen: <https://manpages.debian.org/latest/apache2/a2query.html>.

- Zeige aktivierte Apache-Module an:

`sudo a2query -m`

- Prüfe, ob ein bestimmtes Modul installiert ist:

`sudo a2query -m {{modulname}}`

- Zeige aktivierte virtuelle Hosts an:

`sudo a2query -s`

- Zeige das aktuell aktivierte Multi-Processing-Modul an:

`sudo a2query -M`

- Zeige die Apache-Versionsnummer an:

`sudo a2query -v`
