# git subtree

> Strumento per gestire le dipendenze di un progetto come progetti secondari.
> Maggiori informazioni: <https://manpages.debian.org/latest/git-man/git-subtree.1.html>.

- Aggiungi un repository Git come albero secondario:

`git subtree add --prefix={{percorso/della/directory/}} --squash {{url_repository}} {{master}}`

- Aggiorna l'albero secondario di un repository al suo commit più recente:

`git subtree pull --prefix={{percorso/della/directory/}} {{url_repository}} {{master}}`

- Unisci un albero secondario al ramo principale (master):

`git subtree merge --prefix={{percorso/della/directory/}} --squash {{url_repository}} {{master}}`

- Invia commit all'albero secondario di un repository:

`git subtree push --prefix={{percorso/della/directory/}} {{url_repository}} {{master}}`

- Estrai la cronologia di un nuovo progetto dalla cronologia di un albero secondario:

`git subtree split --prefix={{percorso/della/directory/}} {{url_repository}} -b {{nome_ramo}}`
