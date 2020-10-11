# git mv

> Sposta o rinomina file e aggiorna l'indice Git.
> Maggiori informazioni: <https://git-scm.com/docs/git-mv>.

- Sposta i file nella repository e aggiungi l'operazione al commit successivo:

`git mv {{percorso/al/file}} {{nuovo/percorso/al/file}}`

- Rinomina i file e aggiungi l'operazione al commit successivo:

`git mv {{file}} {{file_rinominato}}`

- Sposta sovrascrivendo eventuali file esistenti nel percorso di destinazione:

`git mv --force {{percorso/al/file}} {{nuovo/percorso/al/file}}`
