# git clone

> Clona un repository esistente.
> Maggiori informazioni: <https://git-scm.com/docs/git-clone>.

- Clona un repository remoto esistente:

`git clone {{url_repository_remoto}}`

- Clona un repository remoto insieme ai suoi sottomoduli:

`git clone --recursive {{url_repository_remoto}}`

- Clona un repository locale:

`git clone -l`

- Clona in modalità silenziosa:

`git clone -q`

- Clona un repository remoto troncando il numero di revisioni a un massimo di 10 per file, cosí da impiegare meno tempo:

`git clone --depth {{10}} {{url_repository_remoto}}`
