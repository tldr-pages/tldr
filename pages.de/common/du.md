# du

> Disk usage: Plattenplatzverbrauch von Dateien und Verzeichnissen ermitteln.
> Weitere Informationen: <https://www.gnu.org/software/coreutils/du>.

- Größe von Verzeichnissen und Unterverzeichnissen in den gegebenen Einheiten (B/KB/MB) auflisten:

`du -{{b|k|m}} {{Pfad/zum/Verzeichnis}}`

- Liste die Größe von Verzeichnissen und Unterverzeichnissen in für Menschen lesbaren Einheiten auf (d. h. die automatische Auswahl der geeigneten Einheit für jede Größe):

`du -h {{Pfad/zum/Verzeichnis}}`

- Zeige die Größe eines Verzeichnisses in für Menschen lesbaren Einheiten:

`du -sh {{Pfad/zum/Verzeichnis}}`

- Liste die Größe eines Verzeichnisses und seiner Dateien in für Menschen lesbaren Einheiten:

`du -ah {{Pfad/zum/Verzeichnis}}`

- Auflistung der menschenlesbaren Größen eines Verzeichnisses und aller Unterverzeichnisse, bis zu einer Tiefe von `N` Ebenen:

`du -h --max-depth=N {{Pfad/zum/Verzeichnis}}`

- Liste die Größe aller `.jpg`-Dateien in Unterverzeichnissen des aktuellen Verzeichnisses auf, in für menschenlesbaren Einheiten und zeige am Ende die kumulierte Gesamtsumme an:

`du -ch */*.jpg`