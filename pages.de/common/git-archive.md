# git archive

> Erstellt ein Archiv von Dateien.
> Mehr Informationen: <https://git-scm.com/docs/git-archive>.

- Erstellt ein Tar-Archiv aus dem Inhalt des aktuellen HEAD und gibt dies aus:

`git archive --verbose HEAD`

- Erstellt ein Zip-Archiv aus dem Inhalt des aktuellen HEAD und gibt dies aus:

`git archive --verbose --format=zip HEAD`

- Wie zuvor, aber nun wir das Zip-Archiv in eine Datei geschrieben:

`git archive --verbose --output={{pfad/zur/datei.zip}} HEAD`

- Erstellt ein Tar-Archiv aus dem Inhalt des letzten Commits eines bestimmten Branches:

`git archive --output={{pfad/zur/datei.tar}} {{branch_name}}`

- Erstellt ein Tar-Archiv von dem Inhalt eines bestimmten Ordners:

`git archive --output={{pfad/zur/datei.tar}} HEAD:{{pfad/zum/ordner}}`

- Jeder Datei wird ein Pfad vorangestellt, um sie in einem bestimmten Verzeichnis zu archivieren:

`git archive --output={{pfad/zur/datei.tar}} --prefix={{pfadh/zum/voranstellen}}/ HEAD`
