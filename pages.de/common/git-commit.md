# git commit

> Commit Dateien in das Repository.
> Mehr Informationen: <https://git-scm.com/docs/git-commit>.

- Commiten von gestagten Dateien zum Repository mit einer Nachricht:

`git commit -m {{message}}`

- Automatisches Stagen aller modifizierten Datei und nachfolgendem Commiten mit einer Nachricht:

`git commit -a -m {{message}}`

- Ersetzt den letzten Commit mit den gerade auf dem Stage liegenden Änderungen:

`git commit --amend`

- Nur spezifische Dateien commiten (die Dateien müssen schon auf dem Stage liegen):

`git commit {{path/to/my/file1}} {{path/to/my/file2}}`
