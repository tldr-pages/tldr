# git rev-list

> Elenca le revisioni (commit) in ordine cronologico inverso.
> Maggiori informazioni: <https://git-scm.com/docs/git-rev-list>.

- Mostra tutti i commit del ramo corrente:

`git rev-list {{HEAD}}`

- Mostra i commit più recenti di una certa data, su uno specifico ramo:

`git rev-list --since={{'2019-12-01 00:00:00'}} {{nome_ramo}}`

- Mostra tutti i commit di unione (merge commit) associati a uno specifico commit:

`git rev-list --merges {{commit}}`
