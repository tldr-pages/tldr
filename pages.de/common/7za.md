# 7za

> Ein Dateiarchivierer mit hoher Kompressionsrate.
> Eine alleinstehende Version von `7z` mit Unterstützung für neuere Archivtypen.
> Weitere Informationen: <https://www.7-zip.org/>.

- Archiviere eine Datei oder ein Verzeichnis:

`7za a {{archiv.7z}} {{pfad/zu/datei_oder_verzeichnis}}`

- Extrahiere eine existierende 7z-Datei:

`7za x {{archiv}}`

- Archiviere mit einem bestimmten Archivtyp:

`7za a -t{{zip|gzip|bzip2|tar}} {{archiv}} {{pfad/zu/datei_oder_verzeichnis}}`

- Gib den Inhalt einer Archivdatei aus:

`7za l {{archiv}}`

- Liste alle verfügbaren Archivtypen auf:

`7za i`
