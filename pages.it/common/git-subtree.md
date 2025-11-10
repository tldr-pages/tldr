# git subtree

> Strumento per gestire le dipendenze di un progetto come progetti secondari.
> Maggiori informazioni: <https://manned.org/git-subtree>.

- Aggiungi un repository Git come albero secondario:

`git subtree add {{[-P|--prefix]}} {{percorso/della/directory}} --squash {{url_repository}} {{master}}`

- Aggiorna l'albero secondario di un repository al suo commit più recente:

`git subtree pull {{[-P|--prefix]}} {{percorso/della/directory}} {{url_repository}} {{master}}`

- Unisci un albero secondario al ramo principale (master):

`git subtree merge {{[-P|--prefix]}} {{percorso/della/directory}} --squash {{url_repository}} {{master}}`

- Invia commit all'albero secondario di un repository:

`git subtree push {{[-P|--prefix]}} {{percorso/della/directory}} {{url_repository}} {{master}}`

- Estrai la cronologia di un nuovo progetto dalla cronologia di un albero secondario:

`git subtree split {{[-P|--prefix]}} {{percorso/della/directory}} {{url_repository}} {{[-b|--branch]}} {{nome_ramo}}`
