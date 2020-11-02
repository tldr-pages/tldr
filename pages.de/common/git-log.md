# git log

> Zeigt die Commit-Historie an.
> Mehr Informationen: <https://git-scm.com/docs/git-log>.

- Zeige die Sequenz der Commits des Git-Repository im aktuellen Ordner, beginnend mit dem aktuellen, an. In umgekehrter chronologischer Reihenfolge:

`git log`

- Zeige die Historie einer bestimmten Datei oder eines Verzeichnisses, inklusive Unterschiede, an:

`git log -p {{pfad/zu/datei_oder_ordner}}`

- Zeige einen Überblick der Commits an, und welche Datei(en) jeweils geändert wurde(n):

`git log --stat`

- Zeige einen Graphen von Commits im aktuellen Branch, wobei jeweils nur die erste Zeile der Commit-Nachricht angezeigt wird:

`git log --oneline --graph`

- Zeige einen Graphen von allen Commits, Tags und Branches im gesamten Repository:

`git log --oneline --decorate --all --graph`

- Zeige nur Commits, deren Commit-Nachricht einen gegebenen Text enthalten (Ohne Beachtung von Groß- und Kleinschreibung):

`git log -i --grep {{suchtext}}`

- Zeige die letzten N Commits eines bestimmten Autors:

`git log -n {{anzahl}} --author={{autor}}`

- Zeige alle Commits zwischen zwei Daten an:

`git log --before={{datum}} --after={{datum}}`
