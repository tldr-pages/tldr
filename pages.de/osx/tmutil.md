# tmutil

> Dienstprogramm zum Verwalten von Time Machine-Backups. Die meisten Befehle erfordern Root-Rechte.
> Weitere Informationen: <https://ss64.com/osx/tmutil.html>.

- Setze ein HFS+ Laufwerk als Backupziel:

`sudo tmutil setdestination {{pfad/zu/einhänge_punkt}}`

- Setze eine APF-Freigabe oder SMB-Freigabe als Backupziel:

`sudo tmutil setdestination "{{protocol://benutzer[:passwort]@host/share}}"`

- Hänge das angegebene Ziel an die Liste der Backupziele an:

`sudo tmutil setdestination -a {{ziel}}`

- Aktiviere automatische Backups:

`sudo tmutil enable`

- Deaktiviere automatische Backups:

`sudo tmutil disable`

- Starte ein Backup im Hintergrund, falls nicht bereits eines läuft:

`sudo tmutil startbackup`

- Starte ein Backup im Vordergrund, falls nicht bereits eines läuft:

`sudo tmutil startbackup -b`

- Stoppe ein laufendes Backup:

`sudo tmutil stopbackup`
