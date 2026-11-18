# git apply

> Integriere eine Patch-Datei und/oder füge sie zum Index hinzu.
> Siehe auch: `git am`.
> Weitere Informationen: <https://git-scm.com/docs/git-apply>.

- Gib Informationen über gepatchte Dateien aus:

`git apply {{[-v|--verbose]}} {{pfad/zu/datei}}`

- Integriere die Patch-Datei und füge sie zum Index hinzu:

`git apply --index {{pfad/zu/datei}}`

- Integriere eine externe Patch-Datei:

`curl {{[-L|--location]}} {{https://example.com/datei.patch}} | git apply`

- Gib diffstat des Inputs aus und integriere die Patch-Datei:

`git apply --stat --apply {{pfad/zu/datei}}`

- Integriere eine Patch-Datei in umgekehrter Reihenfolge:

`git apply {{[-R|--reverse]}} {{pfad/zu/datei}}`

- Speichere das Ergebnis einer Patch-Datei im Index, ohne den Arbeitsbaum zu verändern:

`git apply --cached {{pfad/zu/datei}}`
