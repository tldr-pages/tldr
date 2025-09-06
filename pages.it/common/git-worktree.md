# git worktree

> Gestisci gli alberi di lavoro collegati allo stesso repository.
> Maggiori informazioni: <https://git-scm.com/docs/git-worktree>.

- Crea una nuova directory a partire da uno specifico ramo:

`git worktree add {{percorso/della/directory}} {{ramo}}`

- Crea una nuova directory a partire da un nuovo ramo:

`git worktree add {{percorso/della/directory}} -b {{nuovo_ramo}}`

- Mostra tutte le directory di lavoro collegate al repository corrente:

`git worktree list`

- Cancella un albero di lavoro (dopo averne cancellato la directory):

`git worktree prune`
