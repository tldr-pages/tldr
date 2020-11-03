# git show-branch

> Mostra rami e relativi commit.
> Maggiori informazioni: <https://git-scm.com/docs/git-show-branch>.

- Mostra un sommario degli ultimi commit in un ramo:

`git show-branch {{nome_ramo|riferimento|commit}}`

- Confronta commit nella cronologia di più commit o rami:

`git show-branch {{nome_ramo|riferimento|commit}}`

- Confronta tutti i rami remoti tracciati:

`git show-branch --remotes`

- Confronta i rami locali e remoti:

`git show-branch --all`

- Mostra gli ultimi commit di tutti i rami:

`git show-branch --all --list`

- Confronta un dato ramo con quello corrente:

`git show-branch --current {{commit|nome_ramo|riferimento}}`

- Mostra il nome del commit e non il nome relativo:

`git show-branch --sha1-name --current {{current|nome_ramo|riferimento}}`

- Mostra un numero aggiuntivo di commit oltre il predecessore comune:

`git show-branch --more {{5}} {{commit|nome_ramo|riferimento}} {{commit|nome_ramo|riferimento}} {{...}}`
