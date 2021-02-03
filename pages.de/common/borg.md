# borg

> Deduplizierendes Sicherungswerkzeug.
> Erstellt lokale oder entfernte Sicherungen, die als Dateisysteme mountbar sind.
> Mehr Informationen: <https://borgbackup.readthedocs.io/en/stable/usage/general.html>.

- Initialisiert ein (lokales) Repository:

`borg init {{/pfad/zum/repo_verzeichnis}}`

- Sichern Sie ein Verzeichnis in das Repository und erstellen Sie ein Archiv mit dem Namen "Montag":

`borg create --progress {{/pfad/zum/repo_verzeichnis}}::{{Montag}} {{/pfad/zum/quell_verzeichnis}}`

-  Alle Archive in einem Repository auflisten:

`borg list {{/pfad/zum/repo_verzeichnis}}`

- Extrahieren eines bestimmten Verzeichnisses aus dem "Monday"-Archiv in einem entfernten Repository, unter Ausschluss aller *.ext-Dateien:

`borg extract {{benutzer}}@{{host}}:{{/pfad/zum/repo_verzeichnis}}::{{Montag}} {{/pfad/zum/ziel_verzeichnis} --exclude '{{*.ext}}'`

- Bereinigen Sie ein Repository, indem Sie alle Archive löschen, die älter als 7 Tage sind und Änderungen auflisten:

`borg prune --keep-within {{7d}} --list {{/pfad/zum/repo_verzeichnis}}`

- Mounten Sie ein Repository als FUSE-Dateisystem:

`borg mount {{/pfad/zum/repo_verzeichnis}}::{{Montag}} {{/pfad/zum/mountpoint}}`

- Hilfe zur Erstellung von Archiven anzeigen:

`borg create --help`
