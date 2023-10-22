# git commit

> Salva file nell'area di stage in una nuova istantanea del tuo repository.
> Maggiori informazioni: <https://git-scm.com/docs/git-commit>.

- Committa sul repository i file nell'area di stage con un messaggio:

`git commit -m "{{messaggio}}"`

- Aggiungi all'area di stage tutti i file modificati e committali con un messaggio:

`git commit -a -m "{{messaggio}}"`

- Sostituisci l'ultimo commit con le modifiche attualmente salvate nell'area di stage:

`git commit --amend`

- Committa solo i file specificati (tra quelli presenti nell'area di stage):

`git commit {{percorso/del/file1}} {{percorso/del/file2}}`
