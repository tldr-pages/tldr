# a2query

> Bekomme die geladenen Konfiguration von Apache auf Debian basierten Betriebssystemen.
> Mehr Informationen: <https://manpages.debian.org/buster/apache2/a2query.1.en.html>.

- Liste alle aktivierten Apache Module auf:

`sudo a2query -m`

- Überprüfe ob ein spezifisches Modul installiert ist:

`sudo a2query -m {{module_name}}`

- Liste die aktivierten virtuellen Hosts:

`sudo a2query -s`

- Zeige das aktuell aktivierte Multi Processing Modul:

`sudo a2query -M`

- Zeige die Apache Version:

`sudo a2query -v`
