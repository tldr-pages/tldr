# borg

> Deduplizierendes Sicherungswerkzeug.
> Erstellt lokale oder entfernte Sicherungen, die als Dateisysteme einhängbar sind.
> Weitere Informationen: <https://borgbackup.readthedocs.io/en/stable/usage/general.html>.

- Initialisiere ein lokales Repository:

`borg init {{pfad/zu/repo_verzeichnis}}`

- Sichere ein Verzeichnis in das Repository und erstelle ein Archiv mit dem Namen "Montag":

`borg create --progress {{pfad/zu/repo_verzeichnis}}::{{Montag}} {{pfad/zu/quell_verzeichnis}}`

- Liste alle Archive in einem Repository auf:

`borg list {{pfad/zu/repo_verzeichnis}}`

- Extrahiere ein bestimmtes Verzeichnis aus dem "Montag"-Archiv in einem entfernten Repository, unter Ausschluss aller `*.ext`-Dateien:

`borg extract {{benutzer}}@{{host}}:{{pfad/zu/repo_verzeichnis}}::{{Montag}} {{pfad/zu/ziel_verzeichnis}} --exclude '{{*.ext}}'`

- Bereinige ein Repository, indem alle Archive gelöscht werden, die älter als 7 Tage sind und Änderungen aufweisen:

`borg prune --keep-within {{7d}} --list {{pfad/zu/repo_verzeichnis}}`

- Hänge ein Repository als FUSE-Dateisystem ein:

`borg mount {{pfad/zu/repo_verzeichnis}}::{{Montag}} {{pfad/zu/mountpoint}}`

- Zeige Hilfe zur Erstellung von Archiven an:

`borg create --help`
