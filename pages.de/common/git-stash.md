# git stash

> Speichere lokale Git-Änderungen in einem temporären Bereich.
> Weitere Informationen: <https://git-scm.com/docs/git-stash>.

- Speichere aktuelle Änderungen mit einer Nachricht, ausgenommen neue (nicht verfolgte) Dateien:

`git stash push {{[-m|--message]}} {{stash_nachricht}}`

- Speichere aktuelle Änderungen, einschließlich neuer nicht verfolgter Dateien:

`git stash {{[-u|--include-untracked]}}`

- Wähle interaktiv Teile geänderter Dateien zum Speichern:

`git stash {{[-p|--patch]}}`

- Liste alle Stashes auf (zeigt Stash-Name, den zugehörigen Branch und die Nachricht):

`git stash list`

- Zeige die Änderungen als Patch zwischen dem Stash (Standard ist `stash@{0}`) und dem Commit, als der Stash-Eintrag zum ersten Mal erstellt wurde:

`git stash show {{[-p|--patch]}} {{stash@{0}}}`

- Wende einen Stash an (Standard ist der letzte, benannt `stash@{0}`):

`git stash apply {{optional_stash_name_oder_commit}}`

- Entferne oder wende einen Stash (Standard ist `stash@{0}`) an und entferne ihn aus der Stash-Liste, wenn das Anwenden keine Konflikte verursacht:

`git stash pop {{optional_stash_name}}`

- Entferne alle Stashes:

`git stash clear`
