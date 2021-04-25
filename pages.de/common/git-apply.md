# git apply

> Integriere eine Patch-Datei und/oder füge sie zum Index/Stage hinzu.
> Mehr Informationen: <https://git-scm.com/docs/git-apply>.

- Gib Meldungen über eine gepatchten Datei aus:

`git apply --verbose {{pfad/zu/datei}}`

- Integriere die Patch-Datei und füge sie zum Index/Stage hinzu:

`git apply --index {{pfad/zu/datei}}`

- Integriere eine externe Patch-Datei:

`curl {{https://beispiel.de/datei.patch}} | git apply`
