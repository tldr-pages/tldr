# git add

> Füge Dateien zum Index/Stage hinzu.
> Weitere Informationen: <https://git-scm.com/docs/git-add>.

- Füge eine bestimmte Datei zum Index hinzu:

`git add {{pfad/zu/datei}}`

- Füge alle Dateien zum Index hinzu (nachverfolgte und nicht nachverfolgte):

`git add -A`

- Füge nur nachverfolgte Dateien zum Index hinzu (Updaten des Index):

`git add -u`

- Füge auch Dateien, welche ignoriert werden (`.gitignore`) hinzu:

`git add -f`

- Füge Teile von Dateien zum Index interaktiv hinzu:

`git add -p`

- Füge Teile einer bestimmten Datei interaktiv hinzu:

`git add -p {{pfad/zu/datei}}`

- Füge Dateien zum Index interaktiv hinzu:

`git add -i`
