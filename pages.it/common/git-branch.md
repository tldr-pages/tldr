# git branch

> Il principale comando Git per lavorare con i rami.
> Maggiori informazioni: <https://git-scm.com/docs/git-branch>.

- Elenca i rami locali. Il ramo corrente è evidenziato da un `*`:

`git branch`

- Elenca tutti i rami (locali e remoti):

`git branch -a`

- Crea un nuovo ramo a partire dal commit corrente:

`git branch {{nome_del_ramo}}`

- Crea un nuovo ramo a partire dal commit specificato:

`git branch {{nome_del_ramo}} {{commit_hash}}`

- Rinomina un ramo (non applicabile sul ramo corrente):

`git branch -m {{vecchio_nome}} {{nuovo_nome}}`

- Cancella un ramo locale (non applicabile sul ramo corrente):

`git branch -d {{nome_del_ramo}}`
