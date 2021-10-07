# a2query

> Zeigt Apache Laufzeitkonfigurationen auf Debian-basierten Betriebssystemen an.
> Weitere Informationen: <https://manpages.debian.org/buster/apache2/a2query.1.en.html>.

- Zeige aktivierte Apache Module an:

`sudo a2query -m`

- Prüft, ob ein bestimmtes Modul installiert ist:

`sudo a2query -m {{modulname}}`

- Zeigt aktivierte virtuelle Hosts:

`sudo a2query -s`

- Zeigt das aktuell aktivierte Multi-Processing-Modul an:

`sudo a2query -M`

- Zeigt die Apache Versionsnummer:

`sudo a2query -v`
