# git submodule

> Ispeziona, aggiorna e gestisce moduli secondari (submodule).
> Maggiori informazioni: <https://git-scm.com/docs/git-submodule>.

- Installa specifici moduli secondari di un repository:

`git submodule update --init --recursive`

- Aggiungi un repository Git come modulo secondario:

`git submodule add {{url_repository}}`

- Aggiungi un repository Git come modulo secondario alla directory specificata:

`git submodule add {{url_repository}} {{percorso/della/directory}}`

- Aggiorna tutti i moduli secondari al loro commit più recente:

`git submodule foreach git pull`
