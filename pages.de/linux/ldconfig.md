# ldconfig

> Symbolische Verknüpfungen und Zwischenspeicher für Abhängigkeiten von gemeinsam genutzen Bibliotheken konfigurieren.
> Weitere Informationen: <https://manned.org/ldconfig>.

- Aktualisiere symbolische Verknüpfungen und erstelle den Zwischenspeicher neu (wird normalerweise ausgeführt, wenn eine neue Bibliothek installiert wird):

`sudo ldconfig`

- Aktualisiere die symbolischen Verknüpfungen für ein bestimmtes Verzeichnis:

`sudo ldconfig -n {{pfad/zu/ordner}}`

- Gib die Bibliotheken im Zwichenspeicher aus und prüfe ob eine bestimmte Bibliothek vorhanden ist:

`ldconfig -p | grep {{bibliotheksname}}`
