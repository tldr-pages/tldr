# git worktree

> Gestisci gli alberi di lavoro collegati allo stesso repository.
> Maggiori informazioni: <https://git-scm.com/docs/git-worktree>.

- Crea una nuova cartella a partire da uno specifico ramo:

`git worktree add {{percorso/della/cartella}} {{ramo}}`

- Crea una nuova cartella a partire da un nuovo ramo:

`git worktree add {{percorso/della/cartella}} -b {{nuovo_ramo}}`

- Mostra tutte le cartelle di lavoro collegate al repository corrente:

`git worktree list`

- Cancella un albero di lavoro (dopo averne cancellato la cartella):

`git worktree prune`
