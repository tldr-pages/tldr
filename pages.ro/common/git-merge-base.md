# git merge-base

> Găsește un strămoș comun al două commit-uri.
> Mai multe informații: <https://git-scm.com/docs/git-merge-base>.

- Afișează cel mai bun strămoș comun al două commit-uri:

`git merge-base {{commit_1}} {{commit_2}}`

- Afișează toți cei mai buni strămoși comuni ai două commit-uri:

`git merge-base {{[-a|--all]}} {{commit_1}} {{commit_2}}`

- Verifică dacă un commit este strămoș al unui commit specific:

`git merge-base --is-ancestor {{ancestor_commit}} {{commit}}`
