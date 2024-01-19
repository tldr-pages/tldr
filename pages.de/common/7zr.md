# 7zr

> Ein Dateiarchivierer mit hoher Kompressionsrate.
> Eine alleinstehende Version von `7z`, die nur `.7z` Dateien unterstützt.
> Weitere Informationen: <https://manned.org/7zr>.

- [a]rchiviere eine Datei oder ein Verzeichnis:

`7zr a {{pfad/zu/archiv.7z}} {{pfad/zu/datei_oder_verzeichnis}}`

- Verschlüssle ein vorhandenes Archiv (einschließlich Dateinamen):

`7zr a {{pfad/zu/verschlüsselt.7z}} -p{{passwort}} -mhe={{on}} {{pfad/zu/archiv.7z}}`

- E[x]trahiere ein Archiv und behalte die originale Verzeichnisstruktur bei:

`7zr x {{pfad/zu/archiv.7z}}`

- E[x]trahiere ein Archiv in ein bestimmtes Verzeichnis:

`7zr x {{pfad/zu/archiv.7z}} -o{{pfad/zu/verzeichnis}}`

- E[x]trahiere ein Archiv nach `stdout`:

`7zr x {{pfad/zu/archiv.7z}} -so`

- [l]iste den Inhalt einer Archivdatei auf:

`7zr l {{pfad/zu/archiv.7z}}`
