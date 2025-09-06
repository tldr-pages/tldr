# git clone

> Clona un repository esistente.
> Maggiori informazioni: <https://git-scm.com/docs/git-clone>.

- Clona un repository remoto esistente:

`git clone {{url_repository_remoto}}`

- Clona un repository remoto insieme ai suoi sottomoduli:

`git clone --recursive {{url_repository_remoto}}`

- Clona un repository locale:

`git clone -l {{percorso/del/repository/locale}}`

- Clona in modalità silenziosa:

`git clone -q {{url_repository_remoto}}`

- Clona un repository remoto scaricando solo i 10 commit più recenti del ramo principale (utile per risparmiare tempo):

`git clone --depth {{10}} {{url_repository_remoto}}`
