# git am

> Patch-Dateien integrieren. Nützlich beim Empfang von Commits per E-Mail.
> Siehe auch `git format-patch`, womit Patch-Dateien erzeugen werden können.
> Mehr Informationen: <https://git-scm.com/docs/git-am>.

- Integrieren einer Patch-Datei:

`git am {{pfad/zur/datei.patch}}`

- Prozess zum Integrieren einer Patch-Datei abbrechen:

`git am --abort`

- Integriert soviele Patch-Dateien wie möglich und speichert fehlgeschlagene Teile:

`git am --reject {{pfad/zur/datei.patch}}`
