# bat

> Ausgabe und Verkettung von einzelnen Dateien.
> Ein `cat`-Ersatz mit Syntax-Hervorhebung und Git-Integration.

- Gebe den Inhalt einer Datei in der Standardausgabe aus:

`bat {{file}}`

- Verkette mehrere Dateien in eine Zieldatei:

`bat {{file1}} {{file2}} > {{target_file}}`

- Hänge mehrere Dateien an eine Zieldatei an:

`bat {{file1}} {{file2}} >> {{target_file}}`

- Nummeriere alle ausgegebenen Zeilen:

`bat -n {{file}}`

- Syntax-Hervorhebung für eine json Datei:

`bat --language json {{file.json}}`

- Zeige alle unterstüten Sprachen an:

`bat --list-languages`
