# git checkout

> Wechsle zu einem Branch oder zu Pfaden im Arbeitsverzeichnis.
> Weitere Informationen: <https://git-scm.com/docs/git-checkout>.

- Erstelle und wechsele zu einem neuen Branch:

`git checkout -b {{branch_name}}`

- Erstelle und wechsele zu einem neuen Branch basierend auf einer bestimmten Referenz (Branch, remote/branch und Tag sind Beispiele für gültige Referenzen):

`git checkout -b {{branch_name}} {{reference}}`

- Wechsle zu einem vorhandenen lokalen Branch:

`git checkout {{branch_name}}`

- Wechsle zu dem zuletzt ausgecheckten Branch:

`git checkout -`

- Wechsle zu einem vorhandenen Remote-Branch:

`git checkout {{[-t|--track]}} {{remote_name}}/{{branch_name}}`

- Verwirf alle nicht gestagten Änderungen im aktuellen Verzeichnis (siehe `git reset` für weitere Undo-Befehle):

`git checkout .`

- Verwirf nicht gestagte Änderungen an einer bestimmten Datei:

`git checkout {{pfad/zu/datei}}`

- Ersetze eine Datei im aktuellen Verzeichnis durch die Version, die in einem bestimmten Branch committet wurde:

`git checkout {{branch_name}} -- {{pfad/zu/datei}}`
