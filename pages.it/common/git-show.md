# git show

> Mostra vari tipi di oggetti Git (commit, tag, etc.).
> Maggiori informazioni: <https://git-scm.com/docs/git-show>.

- Mostra informazioni sull'ultimo commit (hash, messaggio, modifiche, ed altri metadati):

`git show`

- Mostra informazioni su un dato commit:

`git show {{commit}}`

- Mostra informazioni sul commit associato ad un tag specifico:

`git show {{tag}}`

- Mostra informazioni sul terzo commit dalla cima del ramo:

`git show {{ramo}}~{{3}}`

- Mostra il messaggio di commit su linea singola, senza mostrare il diff:

`git show --oneline -s {{commit}}`

- Mostra solo la lista dei file modificati in un commit:

`git show --stat {{commit}}`

- Mostra il contenuto di un file ad una data revisione (ad esempio, in un ramo, tag o commit):

`git show {{revisione}}:{{percorso/del/file}}`
