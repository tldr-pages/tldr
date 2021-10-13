# ldconfig

> Symbolische Verknüpfungen und Zwischenspeicher für Abhängigkeiten von gemeinsam genutzen Bibliotheken konfigurieren.
> Configure symlinks and cache for shared library dependencies.
> Weitere Informationen: <https://manned.org/ldconfig>.

- Aktualisiere symbolische Verknüpfungen und erstelle den Zwischenspeicher neu (wird normalerweise ausheführt, wenn eine neue Bibliothek installiert wird):

`sudo ldconfig`

- Aktualisiere die symbolischen Verknüpfungen für ein bestimmtes Verzeichnis:

`sudo ldconfig -n {{path/to/directory}}`

- Gebe die Bibliotheken im Zwichenspeicher aus und prüfe ob eine bestimmte Bibliothek vorhanden ist:

`ldconfig -p | grep {{library_name}}`
