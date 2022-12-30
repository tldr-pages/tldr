# git bundle

> Colloca oggetti e riferimenti in un archivio.
> Maggiori informazioni: <https://git-scm.com/docs/git-bundle>.

- Crea un file bundle che contiene tutti gli oggetti e riferimenti di un dato ramo:

`git bundle create {{percorso/del/file.bundle}} {{nome_ramo}}`

- Crea un file bundle di tutti i rami:

`git bundle create {{percorso/del/file.bundle}} --all`

- Crea un file bundle degli ultimi 5 commit sul ramo corrente:

`git bundle create {{percorso/del/file.bundle}} -{{5}} {{HEAD}}`

- Crea un file bundle degli ultimi 7 giorni:

`git bundle create {{percorso/del/file.bundle}} --since={{7.days}} {{HEAD}}`

- Verifica che un file bundle sia valido e possa essere applicato al repository in uso:

`git bundle verify {{percorso/del/file.bundle}}`

- Stampa su standard output la lista di riferimenti contenuti in un bundle:

`git bundle unbundle {{percorso/del/file.bundle}}`

- Dato un file bundle, estrai un ramo specifico nel repository in uso:

`git pull {{percorso/del/file.bundle}} {{nome_ramo}}`
