# git commit

> Committe Dateien in ein Repository.
> Mehr Informationen: <https://git-scm.com/docs/git-commit>.

- Committe gestagten Dateien zum Repository mit einer Nachricht:

`git commit -m {{nachricht}}`

- Stage alle modifizierten Dateien und comitte sie mit einer Nachricht:

`git commit -a -m {{nachricht}}`

- Ersetze den letzten Commit mit den gerade auf dem Stage liegenden Änderungen:

`git commit --amend`

- Comitte nur spezifische Dateien (die Dateien müssen schon auf dem Stage liegen):

`git commit {{pfad/zu/datei1}} {{pfad/zu/datei2}}`
