# diff

> Vergleiche Dateien und Verzeichnisse.
> Weitere Informationen: <https://man7.org/linux/man-pages/man1/diff.1.html>.

- Vergleiche Dateien (Listet jene Veränderungen auf, mit denen `datei1` zu `datei2` wird):

`diff {{pfad/zu/datei1}} {{pfad/zu/datei2}}`

- Vergleiche Dateien und ignoriere Leerzeichen:

`diff --ignore-all-space {{pfad/zu/datei1}} {{pfad/zu/datei2}}`

- Vergleiche Dateien und zeige Unterschiede nebeneinander:

`diff --side-by-side {{pfad/zu/datei1}} {{pfad/zu/datei2}}`

- Vergleiche Dateien und zeige Unterschiede in vereinheitlichtem Format (wie in `git diff`):

`diff --unified {{pfad/zu/datei1}} {{pfad/zu/datei2}}`

- Vergleiche Verzeichnisse rekursiv (zeigt sowohl Namen von unterschiedlichen Dateien/Verzeichnissen, als auch Unterschiede zwischen Dateien):

`diff --recursive {{altes_verzeichnis}} {{neues_verzeichnis}}`

- Vergleiche Verzeichnisse und zeige nur die Namen der Dateien, die unterschiedlich sind:

`diff --recursive --brief {{altes_verzeichnis}} {{neues_verzeichnis}}`

- Erstelle ein patch-Datei für Git bestehend aus den Unterschieden zweier Dateien und behandle fehlende Dateien als leer:

`diff --text --unified --new-file {{pfad/zu/datei1}} {{pfad/zu/datei2}} > {{pfad/zu/diff.patch}}`
