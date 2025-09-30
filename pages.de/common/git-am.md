# git am

> Patch-Dateien integrieren. Nützlich beim Empfang von Commits per E-Mail.
> Siehe auch `git format-patch` zur Erzeugung von Patch-Dateien.
> Weitere Informationen: <https://git-scm.com/docs/git-am>.

- Integriere eine Patch-Datei:

`git am {{pfad/zu/datei.patch}}`

- Herunterladen und Integrieren einer Patch-Datei:

`curl {{[-L|--location]}} {{https://beispiel.de/datei.patch}} | git apply`

- Brich das Integrieren einer Patch-Datei ab:

`git am --abort`

- Integriere so viele Patch-Dateien wie möglich und speichere fehlgeschlagene Teile:

`git am --reject {{pfad/zu/datei.patch}}`
