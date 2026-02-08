# unzip

> Extrahiere Dateien/Verzeichnisse aus Zip-Archiven.
> Siehe auch: `zip`.
> Weitere Informationen: <https://manned.org/unzip>.

- Extrahiere alle Dateien/Verzeichnisse aus bestimmten Archiven in das aktuelle Verzeichnis:

`unzip {{pfad/zu/archiv1.zip pfad/zu/archiv2.zip ...}}`

- Extrahiere Dateien/Verzeichnisse aus Archiven in einen bestimmten Pfad:

`unzip {{pfad/zu/archiv1.zip pfad/zu/archiv2.zip ...}} -d {{pfad/zu/ausgabe}}`

- Extrahiere Dateien/Verzeichnisse aus Archiven zu `stdout` zusammen mit den extrahierten Dateinamen:

`unzip -c {{pfad/zu/archiv1.zip pfad/zu/archiv2.zip ...}}`

- Extrahiere ein auf Windows erstelltes Archiv, das Dateien mit Nicht-ASCII-Dateinamen enthält (z.B. chinesische oder japanische Zeichen):

`unzip -O {{gbk}} {{pfad/zu/archiv1.zip pfad/zu/archiv2.zip ...}}`

- Liste den Inhalt eines bestimmten Archivs auf, ohne sie zu extrahieren:

`unzip -l {{pfad/zu/archiv}}.zip`

- Extrahiere bestimmte Dateien aus einem Archiv:

`unzip -j {{pfad/zu/archiv}}.zip {{pfad/zu/datei1_im_archiv pfad/zu/datei2_im_archiv ...}}`
