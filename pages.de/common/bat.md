# bat

> Ausgabe und Verkettung von einzelnen Dateien.
> Ein `cat`-Ersatz mit Syntax-Hervorhebung und Git-Integration.
> Weitere Informationen: <https://github.com/sharkdp/bat>.

- Gib den Inhalt einer Datei in `stdout` aus:

`bat {{pfad/zu/datei}}`

- Verkette mehrere Dateien zu einer Zieldatei:

`bat {{pfad/zu/datei1}} {{pfad/zu/datei2}} > {{pfad/zu/ziel_datei}}`

- Hänge mehrere Dateien an eine Zieldatei an:

`bat {{pfad/zu/datei1}} {{pfad/zu/datei2}} >> {{pfad/zu/ziel_datei}}`

- Nummeriere alle ausgegebenen Zeilen:

`bat -n {{pfad/zu/datei}}`

- Hebe die Syntax einer JSON-Datei hervor:

`bat --language {{json}} {{pfad/zu/datei.json}}`

- Zeige alle unterstützten Sprachen an:

`bat --list-languages`
