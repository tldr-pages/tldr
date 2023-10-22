# git checkout

> Cambia rami o ripristina i file dell'albero di lavoro.
> Maggiori informazioni: <https://git-scm.com/docs/git-checkout>.

- Crea e passa ad un nuovo ramo:

`git checkout -b {{nome_ramo}}`

- Crea e passa ad un nuovo ramo a partire dal riferimento specificato (ramo-locale, remote/ramo-remoto, tag sono alcuni esempi di riferimenti validi):

`git checkout -b {{nome_ramo}} {{riferimento}}`

- Passa ad un ramo locale esistente:

`git checkout {{nome_ramo}}`

- Passa ad un ramo remoto esistente:

`git checkout --track {{nome_repository_remoto}}/{{nome_ramo}}`

- Annulla tutte le modifiche nella directory corrente che non sono state aggiunte all'area di stage (vedi `git reset` per più comandi simili):

`git checkout .`

- Annulla tutte le modifiche di un dato file non aggiunte all'area di stage:

`git checkout {{nome_file}}`

- Sostituisci un file con il contenuto del suo corrispondente localizzato su un altro ramo:

`git checkout {{nome_ramo}} -- {{nome_file}}`
