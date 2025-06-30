# find

> Dateien oder Verzeichnisse in einem Verzeichnisbaum rekursiv suchen.
> Weitere Informationen: <https://manned.org/find>.

- Dateien nach Erweiterung suchen:

`find {{root_path}} -name '{{*.ext}}'`

- Sucht nach Dateien, die mehreren Pfad-/Namensmustern entsprechen:

`find {{root_path}} -path '{{*/path/*/*.ext}}' -or -name '{{*pattern*}}'`

- Sucht nach Verzeichnissen, die einem bestimmten Namen entsprechen, ohne Berücksichtigung der Groß- und Kleinschreibung:

`find {{root_path}} -type d -iname '{{*lib*}}'`

- Sucht nach Dateien, die einem bestimmten Muster entsprechen, unter Ausschluss bestimmter Pfade:

`find {{root_path}} -name '{{*.py}}' -not -path '{{*/site-packages/*}}'`

- Sucht nach Dateien, die einem bestimmten Größenbereich entsprechen, wobei die rekursive Tiefe auf "1" begrenzt wird:

`find {{root_path}} -maxdepth 1 -size {{+500k}} -size {{-10M}}`

- Führ für jede Datei einen Befehl aus (verwende `{}` innerhalb des Befehls, um auf den Dateinamen zuzugreifen):

`find {{root_path}} -name '{{*.ext}}' -exec {{wc -l}} {} \;`

- Findet alle heute geänderten Dateien und übergibt die Ergebnisse als Argumente an einen einzelnen Befehl:

`find {{root_path}} -daystart -mtime {{-1}} -exec {{tar -cvf archive.tar}} {} \+`

- Sucht nach leeren Dateien oder Verzeichnissen und löschen Sie diese ausführlich:

`find {{root_path}} -type {{f|d}} -empty -delete -print`
