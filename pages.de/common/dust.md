# dust

> Dust gib einen sofortigen Überblick, welche Verzeichnisse Festplatten Speicherplatz benutzen.
> Weitere Informationen: <https://github.com/bootandy/dust>.

- Informationen für das aktuelle Verzeichnis anzeigen:

`dust`

- Informationen für eine durch Leerzeichen getrennte Liste von Verzeichnissen anzeigen:

`dust {{pfad/zum/verzeichnis1}} {{pfad/zum/verzeichnis2}}`

- 30 Verzeichnisse anzeigen (Standardwert: 21):

`dust --number-of-lines {{30}}`

- Zeigt Informationen für das aktuelle Verzeichnis an, bis zu 3 Ebenen tief:

`dust --depth {{3}}`

- Die größten Verzeichnisse in absteigender Reihenfolge oben anzeigen:

`dust --reverse`

- Alle Dateien und Verzeichnisse mit einem bestimmten Namen ignorieren:

`dust --ignore-directory {{datei_oder_verzeichnis_name}}`

- Keine Prozentbalken und Prozente anzeigen:

`dust --no-percent-bars`
