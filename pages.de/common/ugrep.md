# ugrep

> Ultraschnelles Suchtool mit Abfrage-TUI.
> Weitere Informationen: <https://github.com/Genivia/ugrep>.

- Ausführen das interaktives Suchtool TUI (presse Control-Z um Hilfe):

`ugrep --query`

- Suche rekursiv alle Dateien die ein reguläres Ausdrucksmuster enthalten:

`ugrep "{{SuchMuster}}"`

- Suche rekursiv alle Dateien die ein reguläres Ausdrucksmuster enthalten:

`ugrep --line-number "{{SuchMuster}}" {{path/to/file_or_directory}}`

- Liste der passenden Dateien:

`ugrep --files-with-matches "{{SuchMuster}}"`

- Suche "fuzzy" reguläres Ausdrucksmuster mit maximal 3 zusätzliche, fehlende oder nicht übereinstimmende Zeichen:

`ugrep --fuzzy=3 "{{SuchMuster}}"`

- Suche rekursiv alle komprimierte Dateien, zip- und tar-Archive:

`ugrep --decompress "{{SuchMuster}}"`

- Suche nur Dateien deren Dateinamen mit einem `foo*.???` glob-Muster übereinstimmen:

`ugrep --glob="{{foo*.???}}" "{{SuchMuster}}"`

- Suche nur C++-Quelldateien (verwenden `--type=list` um alle Dateitypen aufzulisten):

`ugrep --type=cpp "{{SuchMuster}}"`
