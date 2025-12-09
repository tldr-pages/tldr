# git rev-parse

> Mostra i metadati relativi a specifiche revisioni.
> Maggiori informazioni: <https://git-scm.com/docs/git-rev-parse>.

- Mostra l'hash del commit di un ramo:

`git rev-parse {{nome_ramo}}`

- Mostra il nome del ramo corrente:

`git rev-parse --abbrev-ref {{HEAD}}`

- Mostra il percorso assoluto della directory di root:

`git rev-parse --show-toplevel`
