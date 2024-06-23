# ugrep

> Ultraschnelles Suchtool mit Abfrage-TUI.
> Weitere Informationen: <https://github.com/Genivia/ugrep>.

- Starte eine interaktive TUI um rekursiv nach Dateien im aktuellen Verzeichnis zu suchen (Strg-Z für Hilfe):

`ugrep --query`

- Suche im aktuellen Verzeichnis rekursiv nach Dateien, die einem bestimmten regulären Ausdruck entsprechen:

`ugrep "{{suchmuster}}"`

- Suche in einer Datei oder in allen Dateien in einem bestimmten Verzeichnis und zeige die Zeilennummer jedes Treffers:

`ugrep --line-number "{{suchmuster}}" {{pfad/zu/datei_oder_verzeichnis}}`

- Suche in allen Dateien im aktuellen Verzeichnis rekursiv und zeige den Dateinamen jeder passenden Datei:

`ugrep --files-with-matches "{{suchmuster}}"`

- Suche nach einem "fuzzy" regulären Ausdruck mit bis zu 3 zusätzlichen, fehlenden oder nicht übereinstimmenden Zeichen:

`ugrep --fuzzy={{3}} "{{suchmuster}}"`

- Suche auch in allen komprimierten Dateien und Zip- und tar-Archive:

`ugrep --decompress "{{suchmuster}}"`

- Suche nur in Dateien deren Dateinamen mit einem bestimmten glob-Muster übereinstimmen:

`ugrep --glob="{{glob_muster}}" "{{suchmuster}}"`

- Suche nur in C++ Quelldateien (verwende `--file-type=list`, um mögliche Optionen aufzulisten):

`ugrep --file-type=cpp "{{suchmuster}}"`
