# git rebase

> Wende Commits von einem Branch auf einen anderen Branch an.
> Die Änderungen eines Branches werden auf einen bestehenden Branch "übertragen" und am Ende der Historie als neue Commits eingefügt.
> Weitere Informationen: <https://git-scm.com/docs/git-rebase>.

- Verwende einen anderen, angegebenen Branch als Basis für den aktuellen Branch:

`git rebase {{new_base_branch}}`

- Starte einen interaktiven Rebase, bei dem Commits umsortiert, weggelassen, kombiniert oder verändert werden können:

`git rebase -i {{target_base_branch_or_commit_hash}}`

- Setze einen Rebase fort, der durch einen Merge Fehler unterbrochen wurde, nachdem die Konflikte aufgelöst wurden:

`git rebase --continue`

- Setze einen Rebase fort, der durch einen Merge Fehler unterbrochen wurde, durch auslassen des in Konflikt stehenden Commits:

`git rebase --skip`

- Brich einen laufenden Rebase ab (z.B. wenn er durch Merge Konflikte unterbrochen wurde):

`git rebase --abort`

- Einen Teil des aktuellen Branches auf eine neue Basis verschieben und dabei die alte Basis angeben, ab der die Änderungen verwendet werden sollen:

`git rebase --onto {{neue_basis}} {{alte_basis}}`

- Interaktiver Rebase der letzten 5 Commits (z.B. um mehrere Commits zusammenzuführen):

`git rebase -i {{HEAD~5}}`

- Konflikte automatisch auflösen, indem der aktuelle Branch bevorzugt wird (das Schlüsselwort `theirs` hat in diesem Fall eine umgekehrte Bedeutung):

`git rebase -X theirs {{branch_name}}`
