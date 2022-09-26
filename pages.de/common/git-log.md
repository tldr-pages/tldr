# git log

> Zeigt die Commit-Historie an.
> Weitere Informationen: <https://git-scm.com/docs/git-log>.

- Zeige die Sequenz der Commits des Git-Repository im aktuellen Verzeichnis, beginnend mit dem aktuellen, an.

`git log`

- Zeige die Historie einer bestimmten Datei oder eines Verzeichnisses, inklusive Unterschiede, an:

`git log -p {{pfad/zu/datei_oder_verzeichnis}}`

- Zeige einen Überblick der Commits an und welche Dateien jeweils verändert wurden:

`git log --stat`

- Zeige einen Graphen von Commits im aktuellen Branch, wobei jeweils nur die erste Zeile der Commit-Nachricht angezeigt wird:

`git log --oneline --graph`

- Zeige einen Graphen von allen Commits, Tags und Branches im gesamten Repository:

`git log --oneline --decorate --all --graph`

- Zeige nur Commits, deren Commit-Nachricht einen bestimmten Text enthalten (Ohne Beachtung von Groß- und Kleinschreibung):

`git log -i --grep {{text}}`

- Zeige die letzten N Commits eines bestimmten Autors:

`git log -n {{anzahl}} --author={{autor}}`

- Zeige alle Commits zwischen zwei Zeitpunkten an (yyyy-mm-dd):

`git log --before="{{2017-01-29}}" --after="{{2017-01-17}}"`
