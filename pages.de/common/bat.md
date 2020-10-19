# bat

> Ausgabe und Verkettung von einzelnen Dateien.
> Ein `cat`-Ersatz mit Syntax-Hervorhebung und Git-Integration.

- Gebe den Inhalt einer Datei in der Standardausgabe aus:

`bat {{datei}}`

- Verkette mehrere Dateien in eine Zieldatei:

`bat {{datei1}} {{datei2}} > {{ziel_datei}}`

- Hänge mehrere Dateien an eine Zieldatei an:

`bat {{datei1}} {{datei2}} >> {{ziel_datei}}`

- Nummeriere alle ausgegebenen Zeilen:

`bat -n {{datei}}`

- Syntax-Hervorhebung für eine json Datei:

`bat --language json {{datei.json}}`

- Zeige alle unterstüten Sprachen an:

`bat --list-languages`
