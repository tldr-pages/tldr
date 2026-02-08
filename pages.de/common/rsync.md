# rsync

> Übertrage Dateien zu oder von einem Remote-Host (aber nicht zwischen zwei Remote-Hosts), verwendet standardmäßig SSH.
> Um einen Remote-Pfad anzugeben, verwende `user@host:pfad/zu/datei_oder_verzeichnis`.
> Weitere Informationen: <https://download.samba.org/pub/rsync/rsync.1>.

- Übertrage eine Datei (verwende `--dry-run`, um die Übertragung zu simulieren):

`rsync {{pfad/zu/quelle}} {{pfad/zu/ziel}}`

- Verwende den Archiv-Modus (kopiere Verzeichnisse rekursiv, kopiere Symlinks ohne Auflösung und behalte Berechtigungen, Eigentum und Änderungszeiten):

`rsync {{[-a|--archive]}} {{pfad/zu/quelle}} {{pfad/zu/ziel}}`

- Komprimiere die Daten beim Senden an das Ziel, zeige ausführlichen und menschenlesbaren Fortschritt und behalte teilweise übertragene Dateien bei Unterbrechung:

`rsync {{[-zvhP|--compress --verbose --human-readable --partial --progress]}} {{pfad/zu/quelle}} {{pfad/zu/ziel}}`

- Kopiere Verzeichnisse rekursiv und stelle sicher, dass jede Datei vollständig auf die Festplatte geschrieben wird, anstatt im RAM zu verbleiben:

`rsync {{[-r|--recursive]}} --fsync {{pfad/zu/quelle}} {{pfad/zu/ziel}}`

- Übertrage Verzeichnisinhalte, aber nicht das Verzeichnis selbst:

`rsync {{[-r|--recursive]}} {{pfad/zu/quelle}}/ {{pfad/zu/ziel}}`

- Verwende den Archiv-Modus, löse Symlinks auf und überspringe Dateien, die im Ziel neuer sind:

`rsync {{[-auL|--archive --update --copy-links]}} {{pfad/zu/quelle}} {{pfad/zu/ziel}}`

- Übertrage ein Verzeichnis von einem Remote-Host, auf dem `rsyncd` läuft, und lösche Dateien im Ziel, die nicht in der Quelle existieren:

`rsync {{[-r|--recursive]}} --delete rsync://{{host}}:{{pfad/zu/quelle}} {{pfad/zu/ziel}}`

- Übertrage eine Datei über SSH unter Verwendung eines anderen Ports als dem Standard (22) und zeige den globalen Fortschritt:

`rsync {{[-e|--rsh]}} 'ssh -p {{port}}' --info=progress2 {{host}}:{{pfad/zu/quelle}} {{pfad/zu/ziel}}`
