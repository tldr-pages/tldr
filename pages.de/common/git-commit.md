# git commit

> Committe Dateien in ein Repository.
> Weitere Informationen: <https://git-scm.com/docs/git-commit>.

- Committe gestagten Dateien zum Repository mit einer Nachricht:

`git commit -m "{{nachricht}}"`

- Committe alle gestagten Dateien zum Repository mit einer Nachricht aus einer Datei:

`git commit --file {{pfad/zu/commit_nachricht_datei}}`

- Stage alle modifizierten Dateien und committe sie mit einer Nachricht:

`git commit -a -m "{{nachricht}}"`

- Committe alle gestagten Dateien und [S]igniere sie mit dem in `~/.gitconfig` definierten GPG Schlüssel:

`git commit -S -m "{{nachricht}}"`

- Ersetze den letzten Commit mit den gerade auf dem Stage liegenden Änderungen:

`git commit --amend`

- Comitte nur spezifische Dateien (die Dateien müssen schon auf dem Stage liegen):

`git commit {{pfad/zu/datei1}} {{pfad/zu/datei2}}`

- Erzeuge einen Commit, auch wenn keine Dateien auf dem Stage liegen:

`git commit -m "{{nachricht}}" --allow-empty`
