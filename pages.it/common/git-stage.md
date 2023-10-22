# git stage

> Aggiungi file all'area di stage.
> Sinonimo di `git add`.
> Maggiori informazioni: <https://git-scm.com/docs/git-stage>.

- Aggiungi un file all'indice:

`git stage {{percorso/del/file}}`

- Aggiungi tutti i file (tracciati e non):

`git stage -A`

- Aggiungi solo file già tracciati:

`git stage -u`

- Aggiungi anche file ignorati:

`git stage -f`

- Aggiungi parti di file all'area di stage in modo interattivo:

`git stage -p`

- Aggiungi parti di un dato file all'area di stage in modo interattivo:

`git stage -p {{percorso/del/file}}`

- Aggiungi all'area di stage in modo interattivo:

`git stage -i`
