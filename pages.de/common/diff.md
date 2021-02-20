# diff

> Vergleiche Dateien und Verzeichnisse.
> Mehr Informationen: <https://man7.org/linux/man-pages/man1/diff.1.html>.

- Vergleiche Dateien (Listet jene Veränderungen auf, mit denen `alte_datei` zu `neue_datei` wird):

`diff {{alte_datei}} {{neue_datei}}`

- Vergleiche Dateien und ignoriere Leerzeichen:

`diff -w {{alte_datei}} {{neue_datei}}`

- Vergleiche Dateien und zeige Unterschiede nebeneinander:

`diff -y {{alte_datei}} {{neue_datei}}`

- Vergleiche Dateien und zeige Unterschiede in vereinheitlichtem Format (wie in `git diff`):

`diff -u {{alte_datei}} {{neue_datei}}`

- Vergleiche Verzeichnisse rekursiv (zeigt sowohl Namen von unterschiedlichen Dateien/Verzeichnissen, als auch Unterschiede zwischen Dateien):

`diff -r {{altes_verzeichnis}} {{neues_verzeichnis}}`

- Vergleiche Verzeichnisse und zeige nur die Namen der Dateien, die unterschiedlich sind:

`diff -rq {{altes_verzeichnis}} {{neues_verzeichnis}}`
