# git add

> Fügt Dateien zum Index/Stage hinzu.
> Mehr Informationen: <https://git-scm.com/docs/git-add>.

- Fügt eine Datei zum Index/Stage hinzu:

`git add {{pfad/zur/datei}}`

- Fügt alle Dateien zum Index/Stage hinzu (nachverfolgte und nicht nachverfolgte):

`git add -A`

- Fügt nur nachverfolgte Dateien zum Index/Stage hinzu (Updaten des Index/Stage):

`git add -u`

- Fügt auch Dateien, welche ignoriert werden (`.gitignore`) hinzu:

`git add -f`

- Interaktives Hinzufügen von Dateien zum Index/Stage:

`git add -p`

- Interaktives Hinzufügen von Teilen der Datei, welche angegeben wird:

`git add -p {{pfad/zur/datei}}`

- Interaktives Hinzufügen von Dateien zum Index/Stage:

`git add -i`
