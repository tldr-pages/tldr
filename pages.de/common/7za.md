# 7za

> Ein Dateiarchivierer mit hoher Kompressionsrate.
> Eine alleinstehende Version von `7z` mit Unterstützung für neuere Archivtypen.
> Weitere Informationen: <https://www.7-zip.org>.

- [a]rchiviere eine Datei oder ein Verzeichnis:

`7za a {{pfad/zu/archiv.7z}} {{pfad/zu/datei_oder_verzeichnis}}`

- Verschlüssle ein vorhandenes Archiv (einschließlich Dateinamen):

`7za a {{pfad/zu/verschlüsselt.7z}} -p{{passwort}} -mhe=on {{pfad/zu/archiv.7z}}`

- E[x]trahiere ein Archiv und behalte die originale Verzeichnisstruktur bei:

`7za x {{pfad/zu/archiv.7z}}`

- E[x]trahiere ein Archiv in ein bestimmtes Verzeichnis:

`7za x {{pfad/zu/archiv.7z}} -o{{pfad/zu/verzeichnis}}`

- E[x]trahiere ein Archiv nach stdout:

`7za x {{pfad/zu/archiv.7z}} -so`

- [a]rchiviere mit einem bestimmten Archivtyp:

`7za a -t{{7z|bzip2|gzip|lzip|tar|zip}} {{pfad/zu/archiv.7z}} {{pfad/zu/datei_oder_verzeichnis}}`

- [l]iste den Inhalt einer Archivdatei auf:

`7za l {{pfad/zu/archiv.7z}}`

- Liste alle verfügbaren Archivtypen auf:

`7za i`
