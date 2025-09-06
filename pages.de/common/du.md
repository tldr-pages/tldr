# du

> Disk usage: Plattenplatzverbrauch von Dateien und Verzeichnissen ermitteln.
> Weitere Informationen: <https://www.gnu.org/software/coreutils/manual/html_node/du-invocation.html>.

- Liste die Größe von Verzeichnissen und Unterverzeichnissen in den gegebenen Einheiten (B/KiB/MiB) auf:

`du -{{b|k|m}} {{pfad/zu/verzeichnis}}`

- Liste die Größe von Verzeichnissen und Unterverzeichnissen in menschenlesbaren Einheiten auf (d.h. automatische Auswahl der geeigneten Einheit für jede Größe):

`du {{[-h|--human-readable]}} {{pfad/zu/verzeichnis}}`

- Zeige die Größe eines einzelnen Verzeichnisses in menschenlesbaren Einheiten:

`du {{[-sh|--summarize --human-readable]}} {{pfad/zu/verzeichnis}}`

- Liste die Größe von Verzeichnissen und Unterverzeichnissen und aller ihrer Dateien in menschenlesbaren Einheiten auf:

`du {{[-ah|--all --human-readable]}} {{pfad/zu/verzeichnis}}`

- Liste die menschenlesbaren Größen eines Verzeichnisses und aller Unterverzeichnisse, bis zu einer Tiefe von `N` Ebenen:

`du {{[-h|--human-readable]}} {{[-d|--max-depth]}} N {{pfad/zu/verzeichnis}}`

- Liste die menschenlesbare Größe aller `.jpg`-Dateien in Unterverzeichnissen des aktuellen Verzeichnisses auf und zeige am Ende die kumulierte Gesamtsumme an:

`du {{[-ch|--total --human-readable]}} {{*/*.jpg}}`
