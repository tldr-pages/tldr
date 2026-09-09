# git update-ref

> Commande Git pour créer, mettre à jour et supprimer des références Git.
> Plus d'informations : <https://git-scm.com/docs/git-update-ref>.

- Supprime une référence, utile pour la réinitialisation du premier commit :

`git update-ref -d {{HEAD}}`

- Met à jour une référence avec un message :

`git update-ref -m {{message}} {{HEAD}} {{4e95e05}}`
