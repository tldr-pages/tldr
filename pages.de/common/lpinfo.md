# lpinfo

> Liste verbundene Drucker und installierte Treiber für den CUPS Druckserver.
> Weitere Informationen: <https://www.cups.org/doc/man-lpinfo.html>.

- Liste alle aktuell verbundenen Drucker auf:

`lpinfo -v`

- Liste alle aktuell installierten Druckertreiber auf:

`lpinfo -m`

- Suche installierte Druckertreiber nach Hersteller oder Modell:

`lpinfo --make-and-model "{{druckermodell}}" -m`
