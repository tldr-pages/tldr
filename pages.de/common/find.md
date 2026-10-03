# find

> Dateien oder Verzeichnisse in einem Verzeichnisbaum rekursiv suchen.
> Siehe auch: `fd`.
> Weitere Informationen: <https://manned.org/find>.

- Dateien nach Erweiterung suchen:

`find {{path/to/directory}} -name '{{*.ext}}'`

- Suche Dateien, die mehreren Pfad-/Namensmustern entsprechen:

`find {{path/to/directory}} -path '{{*/path/*/*.ext}}' -or -name '{{*pattern*}}'`

- Suche Verzeichnisse, die ohne Berücksichtigung der Groß- und Kleinschreibung einem bestimmten Namensmustern entsprechen:

`find {{path/to/directory}} -type d -iname '{{*lib*}}'`

- Suche Dateien, die einem bestimmten Namensmustern entsprechen, unter Ausschluss bestimmter Pfade:

`find {{path/to/directory}} -name '{{*.py}}' -not -path '{{*/site-packages/*}}'`

- Suche Dateien, die einem bestimmten Größenbereich entsprechen, wobei die rekursive Tiefe auf "1" begrenzt wird:

`find {{path/to/directory}} -maxdepth 1 -size {{+500k}} -size {{-10M}}`

- Führe für jede Datei einen Befehl aus (verwende `{}` innerhalb des Befehls, um auf den Dateinamen zuzugreifen):

`find {{path/to/directory}} -name '{{*.ext}}' -exec {{wc -l}} {} \;`

- Finde alle heute geänderten Dateien und übergebe die Ergebnisse als Argumente an einen einzelnen Befehl:

`find {{path/to/directory}} -daystart -mtime {{-1}} -exec {{tar -cvf archive.tar}} {} \+`

- Suche leere Dateien oder Verzeichnisse, gebe diese aus und lösche diese:

`find {{path/to/directory}} -type {{f|d}} -empty -delete -print`
