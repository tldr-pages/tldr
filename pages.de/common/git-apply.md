# git apply

> Integriert eine Patch-Datei und/oder fügt sie zum Index/Stage hinzu.
> Mehr Informationen: <https://git-scm.com/docs/git-apply>.

- Gibt Meldungen über die gepatchten Dateien aus:

`git apply --verbose {{pfad/zur/datei}}`

- Integriert die Patch-Datei und fügt sie zum Index/Stage hinzu:

`git apply --index {{pfad/zur/datei}}`

- Integriert eine externe Patch-Datei:

`curl {{https://example.com/file.patch}} | git apply`
