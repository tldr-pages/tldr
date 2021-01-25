# tmutil

> Dienstprogramm zum Verwalten von Time Machine-Backups. Die meisten Kommandos erfordern Root-Rechte.
> Mehr Informationen: <https://ss64.com/osx/tmutil.html>.

- Setze ein HFS+ Laufwerk als Backupziel:

`sudo tmutil setdestination {{path/to/disk_mount_point}}`

- Setzen von einer APF-Freigabe oder SMB-Freigabe, als Backupziel:

`sudo tmutil setdestination {{protocol://user[:password]@host/share}}`

- Hängen Sie das angegebene Ziel an die Liste der Backupziele an:

`sudo tmutil setdestination -a {{destination}}`

- Aktivieren von automatischen Backups:

`sudo tmutil enable`

- Automatische Backups deaktivieren:

`sudo tmutil disable`

- Starte ein Backup im Hintergrund, falls nicht bereits eines läuft:

`sudo tmutil startbackup`

- Starte ein Backup im Vordergrund, falls nicht bereits eines läuft:

`sudo tmutil startbackup -b`

- Stoppen vom Backup:

`sudo tmutil stopbackup`
