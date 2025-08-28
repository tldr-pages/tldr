# git fetch

> Scarica oggetti e riferimenti da un repository remoto.
> Maggiori informazioni: <https://git-scm.com/docs/git-fetch>.

- Scarica le ultime modifiche dal repository remoto di origine (upstream) di default, se definito:

`git fetch`

- Scarica i nuovi rami da un dato repository remoto di origine:

`git fetch {{nome_repository_remoto}}`

- Scarica le ultime modifiche da tutti i repository remoti di origine:

`git fetch --all`

- Scarica anche i tag dal repository remoto di origine:

`git fetch {{[-t|--tags]}}`

- Elimina i riferimenti locali ai rami remoti che sono stati eliminati dal repositoy di origine:

`git fetch {{[-p|--prune]}}`
