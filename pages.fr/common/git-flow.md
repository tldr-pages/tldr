# git flow

> Une collection d'extensions Git pour procurer des opérations supplémentaires sur les dépôts.
> Plus d'informations : <https://github.com/nvie/gitflow>.

- Initialiser dans un registre Git existant :

`git flow init`

- Commencer le travail sur une fonctionnalité basé sur la branche `develop` :

`git flow feature start {{feature}}`

- Terminer le travail sur une branche de fonctionnalité, la fusionner dans la branche `develop` puis la supprimer :

`git flow feature finish {{feature}}`

- Publier une fonctionnalité sur le serveur distant :

`git flow feature publish {{feature}}`

- Récupérer une fonctionnalité publiée par un autre utilisateur :

`git flow feature pull origin {{feature}}`
