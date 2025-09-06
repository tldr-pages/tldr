# git restore

> Ripristina i file dell'albero di lavoro. Richiede versioni di Git successive alla 2.23.
> Vedi anche `git checkout`.
> Maggiori informazioni: <https://git-scm.com/docs/git-restore>.

- Ripristina un file cancellato dal contenuto del commit corrente (HEAD):

`git restore {{percorso/del/file}}`

- Ripristina un file alla versione di un commit differente:

`git restore --source {{commit}} {{percorso/del/file}}`

- Annulla le modifiche ai file nell'area di stage, ripristinandoli all'HEAD:

`git restore .`
