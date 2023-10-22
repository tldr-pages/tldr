# git reset

> Annulla commit o rimuovi modifiche dall'area di stage, reimpostando l'HEAD corrente su uno specifico stato.
> Se viene fornito un percorso, il comando reset si interpreta come "rimuovi dall'area di stage"; se viene fornito l'hash di un commit o un ramo, si interpreta come "annulla commit".
> Maggiori informazioni: <https://git-scm.com/docs/git-reset>.

- Rimuovi tutto dall'area di stage:

`git reset`

- Rimuovi dall'area di stage uno o più file:

`git reset {{percorso/del/file1}} {{percorso/del/file2}}`

- Rimuovi dall'area di stage solo alcune porzioni di un file in modo interattivo:

`git reset --patch {{percorso/del/file}}`

- Annulla l'ultimo commit, preservando tutte le modifiche nel filesystem:

`git reset HEAD~`

- Annulla gli ultimi due commit, aggiungendo all'area di stage le modifiche relative:

`git reset --soft HEAD~2`

- Annulla le modifiche non committate, indipendentemente se siano presenti nell'area di stage o meno (usa `git checkout` per queste ultime):

`git reset --hard`

- Reimposta il repository su un dato commit, annullando qualsiasi tipo di modifica precedente:

`git reset --hard {{commit}}`
