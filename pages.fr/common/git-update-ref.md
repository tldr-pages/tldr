# git update-ref

> Commande Git pour créer, mettre à jour et supprimer des références Git.
> Plus d'informations : <https://git-scm.com/docs/git-update-ref>.

- Supprimer une référence, utile pour la réinitialisation du premier commit :

`git update-ref -d {{HEAD}}`

- Mettre a jour une référence avec un message :

`git update-ref -m {{message}} {{HEAD}} {{4e95e05}}`
