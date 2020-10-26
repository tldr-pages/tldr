# phpbu

> Ein Backup framework für PHP.
> Mehr informationen: <https://phpbu.de>.

- Backups mit der Standard "phpbu.xml" Konfigurationsdatei ausführen:

`phpbu`

- Backups mit einer spezifischen Konfigurationsdatei ausführen:

`phpbu --configuration={{path/to/configuration_file.xml}}`

- Nur die angegebenen Backups ausführen:

`phpbu --limit={{backup_task_name}}`

- Aktionen die ausgeführt worden wären simulieren:

`phpbu --simulate`
