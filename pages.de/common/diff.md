# diff

> Vergleiche Dateien und Verzeichnisse.
> Weitere Informationen: <https://man7.org/linux/man-pages/man1/diff.1.html>.

- Vergleiche Dateien (Listet jene Veränderungen auf, mit denen `datei1` zu `datei2` wird):

`diff {{pfad/zu/datei1}} {{pfad/zu/datei2}}`

- Vergleiche Dateien und ignoriere Leerzeichen:

`diff -w {{pfad/zu/datei1}} {{pfad/zu/datei2}}`

- Vergleiche Dateien und zeige Unterschiede nebeneinander:

`diff -y {{pfad/zu/datei1}} {{pfad/zu/datei2}}`

- Vergleiche Dateien und zeige Unterschiede in vereinheitlichtem Format (wie in `git diff`):

`diff -u {{pfad/zu/datei1}} {{pfad/zu/datei2}}`

- Vergleiche Verzeichnisse rekursiv (zeigt sowohl Namen von unterschiedlichen Dateien/Verzeichnissen, als auch Unterschiede zwischen Dateien):

`diff -r {{altes_verzeichnis}} {{neues_verzeichnis}}`

- Vergleiche Verzeichnisse und zeige nur die Namen der Dateien, die unterschiedlich sind:

`diff -rq {{altes_verzeichnis}} {{neues_verzeichnis}}`
