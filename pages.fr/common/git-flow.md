# git flow

> Une collection d'extensions Git pour procurer des opérations supplémentaires sur les dépôts.
> Plus d'informations : <https://github.com/nvie/gitflow>.

- Initialise dans un registre Git existant :

`git flow init`

- Commence le travail sur une fonctionnalité basé sur la branche `develop` :

`git flow feature start {{feature}}`

- Termine le travail sur une branche de fonctionnalité, la fusionne dans la branche `develop` puis la supprime :

`git flow feature finish {{feature}}`

- Publie une fonctionnalité sur le serveur distant :

`git flow feature publish {{feature}}`

- Récupère une fonctionnalité publiée par un autre utilisateur :

`git flow feature pull origin {{feature}}`
