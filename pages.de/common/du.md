# du

> Disk usage: Plattenplatzverbrauch von Dateien und Verzeichnissen ermitteln.
> Weitere Informationen: <https://www.gnu.org/software/coreutils/du>.

- Größe von Verzeichnissen und Unterverzeichnissen in den gegebenen Einheiten (B/KB/MB) auflisten:

`du -{{b|k|m}} {{pfad/zu/verzeichnis}}`

- Liste die Größe von Verzeichnissen und Unterverzeichnissen in menschenlesbaren Einheiten auf (d.h. automatische Auswahl der geeigneten Einheit für jede Größe):

`du -h {{pfad/zu/verzeichnis}}`

- Zeige die Größe eines einzelnen Verzeichnisses in menschenlesbaren Einheiten:

`du -sh {{pfad/zu/verzeichnis}}`

- Liste die Größe eines Verzeichnisses und seiner Dateien in menschenlesbaren Einheiten:

`du -ah {{pfad/zu/verzeichnis}}`

- Auflistung der menschenlesbaren Größen eines Verzeichnisses und aller Unterverzeichnisse, bis zu einer Tiefe von `N` Ebenen:

`du -h --max-depth=N {{pfad/zu/verzeichnis}}`

- Liste die menschenlesbare Größe aller `.jpg`-Dateien in Unterverzeichnissen des aktuellen Verzeichnisses auf und zeige am Ende die kumulierte Gesamtsumme an:

`du -ch */*.jpg`
