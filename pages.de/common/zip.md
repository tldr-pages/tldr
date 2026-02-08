# zip

> Verpacke und komprimiere (archiviere) Dateien in ein Zip-Archiv.
> Siehe auch: `unzip`.
> Weitere Informationen: <https://manned.org/zip>.

- Füge Dateien/Verzeichnisse zu einem bestimmten Archiv hinzu:

`zip {{[-r|--recurse-paths]}} {{pfad/zu/komprimiert.zip}} {{pfad/zu/datei_oder_verzeichnis1 pfad/zu/datei_oder_verzeichnis2 ...}}`

- Entferne Dateien/Verzeichnisse aus einem bestimmten Archiv:

`zip {{[-d|--delete]}} {{pfad/zu/komprimiert.zip}} {{pfad/zu/datei_oder_verzeichnis1 pfad/zu/datei_oder_verzeichnis2 ...}}`

- Archiviere Dateien/Verzeichnisse unter Ausschluss bestimmter Dateien:

`zip {{[-r|--recurse-paths]}} {{pfad/zu/komprimiert.zip}} {{pfad/zu/datei_oder_verzeichnis1 pfad/zu/datei_oder_verzeichnis2 ...}} {{[-x|--exclude]}} {{pfad/zu/ausgeschlossene_dateien_oder_verzeichnisse}}`

- Archiviere Dateien/Verzeichnisse mit einem bestimmten Komprimierungslevel (`0` - der niedrigste, `9` - der höchste):

`zip {{[-r|--recurse-paths]}} -{{0..9}} {{pfad/zu/komprimiert.zip}} {{pfad/zu/datei_oder_verzeichnis1 pfad/zu/datei_oder_verzeichnis2 ...}}`

- Erstelle ein verschlüsseltes Archiv mit einem bestimmten Passwort:

`zip {{[-re|--recurse-paths --encrypt]}} {{pfad/zu/komprimiert.zip}} {{pfad/zu/datei_oder_verzeichnis1 pfad/zu/datei_oder_verzeichnis2 ...}}`

- Archiviere Dateien/Verzeichnisse in ein Mehrteil-Split-Zip-Archiv (z.B. 3 GB Teile):

`zip {{[-rs|--recurse-paths --split-size]}} {{3g}} {{pfad/zu/komprimiert.zip}} {{pfad/zu/datei_oder_verzeichnis1 pfad/zu/datei_oder_verzeichnis2 ...}}`

- Gib den Inhalt eines bestimmten Archivs aus:

`zip {{[-sf|--split-size --freshen]}} {{pfad/zu/komprimiert.zip}}`
