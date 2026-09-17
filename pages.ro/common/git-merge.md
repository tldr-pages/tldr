# git merge

> Fuzionează ramuri.
> Mai multe informații: <https://git-scm.com/docs/git-merge>.

- Fuzionează o ramură în ramura ta curentă:

`git merge {{branch_name}}`

- Editează mesajul de fuziune:

`git merge {{[-e|--edit]}} {{branch_name}}`

- Fuzionează o ramură și creează un commit de fuziune:

`git merge --no-ff {{branch_name}}`

- Anulează o fuziune în caz de conflicte:

`git merge --abort`

- Fuzionează folosind o strategie specifică:

`git merge {{[-s|--strategy]}} {{strategy}} {{[-X|--strategy-option]}} {{strategy_option}} {{branch_name}}`
