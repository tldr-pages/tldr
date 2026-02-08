# git merge

- Merge einen Branch in deinen aktuellen Branch:

`git merge {{branch_name}}`

- Bearbeite die Merge-Nachricht:

`git merge {{[-e|--edit]}} {{branch_name}}`

- Merge einen Branch und erstelle einen Merge-Commit:

`git merge --no-ff {{branch_name}}`

- Breche einen Merge ab, falls Konflikte auftreten:

`git merge --abort`

- Merge unter Verwendung einer bestimmten Strategie:

`git merge {{[-s|--strategy]}} {{strategie}} {{[-X|--strategy-option]}} {{strategie_option}} {{branch_name}}`
