# git subtree

> Strumento per gestire le dipendenze di un progetto come progetti secondari.
> Maggiori informazioni: <https://manpages.debian.org/testing/git-man/git-subtree.1.en.html>.

- Aggiungi un repository Git come albero secondario:

`git subtree add --prefix={{percorso/alla/cartella/}} --squash {{url_repository}} {{master}}`

- Aggiorna l'albero secondario di un repository al suo commit più recente:

`git subtree pull --prefix={{percorso/alla/cartella/}} {{url_repository}} {{master}}`

- Unisci un albero secondario al ramo principale (master):

`git subtree merge --prefix={{percorso/alla/cartella/}} --squash {{url_repository}} {{master}}`

- Invia commit all'albero secondario di un repository:

`git subtree push --prefix={{percorso/alla/cartella/}} {{url_repository}} {{master}}`

- Estrai la cronologia di un nuovo progetto dalla cronologia di un albero secondario:

`git subtree split --prefix={{percorso/alla/cartella/}} {{url_repository}} -b {{nome_ramo}}`
