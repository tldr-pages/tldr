# rar

> Der RAR-Archivierer. Unterstützt mehrvolumige Archive, die optional selbstextrahierend sein können.
> Weitere Informationen: <https://manned.org/rar>.

- Archiviere 1 oder mehrere Dateien:

`rar a {{pfad/zu/archivname.rar}} {{pfad/zu/datei1 pfad/zu/datei2 pfad/zu/datei3 ...}}`

- Archiviere ein Verzeichnis:

`rar a {{pfad/zu/archivname.rar}} {{pfad/zu/verzeichnis}}`

- Teile das Archiv in Teile gleicher Größe auf (50M):

`rar a -v{{50M}} -R {{pfad/zu/archivname.rar}} {{pfad/zu/datei_oder_verzeichnis}}`

- Schütze das resultierende Archiv mit einem Passwort:

`rar a -p{{passwort}} {{pfad/zu/archivname.rar}} {{pfad/zu/datei_oder_verzeichnis}}`

- Verschlüssele Dateidaten und Header mit Passwort:

`rar a -hp{{passwort}} {{pfad/zu/archivname.rar}} {{pfad/zu/datei_oder_verzeichnis}}`

- Verwende einen bestimmten Komprimierungslevel (0-5):

`rar a -m{{komprimierungslevel}} {{pfad/zu/archivname.rar}} {{pfad/zu/datei_oder_verzeichnis}}`
