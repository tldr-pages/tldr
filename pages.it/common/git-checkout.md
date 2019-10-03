# git checkout

> Cambia rami o ripristina i file dell'albero di lavoro.
> Maggiori informazioni: <https://git-scm.com/docs/git-checkout>.

- Crea e passa ad un nuovo ramo:

`git checkout -b {{nome_del_ramo}}`

- Crea e passa ad un nuovo ramo a partire dal riferimento specificato (alcuni esempi di riferimenti validi sono rami, rami remoti, tag):

`git checkout -b {{nome_del_ramo}} {{riferimento}}`

- Passa ad un ramo locale esistente:

`git checkout {{nome_del_ramo}}`

- Passa ad un ramo remoto esistente:

`git checkout --track {{nome_repository_remoto}}/{{nome_del_ramo}}`

- Elimina tutte le modifiche che non sono state aggiunte all'indice (vedi `git reset` per comandi simili):

`git checkout .`

- Elimina da un dato file tutte le modifiche che non sono state aggiunte all'indice:

`git checkout {{nome_file}}`

- Sostituisci un file con il contenuto del suo corrispondente localizzato su un altro ramo:

`git checkout {{nome_del_ramo}} -- {{nome_file}}`
