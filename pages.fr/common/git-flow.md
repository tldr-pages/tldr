# git flow

> Une colletion d'extentions Git pour procurer des opperation de registre supplementaires
> Plus d'informations : <https://github.com/nvie/gitflow>.

- Initialiser dans un registre Git existant :

`git flow init`

- Commencer le travail sur une fonctionnalité basé sur la branche `develop` :

`git flow feature start {{feature}}`

- Terminer le travail sur une branche de fonctionnalité, le merger dans la branche `develop` puis suprimmer :

`git flow feature finish {{feature}}`

- Publier une fonctionalité sur le serveur distant :

`git flow feature publish {{feature}}`

- Recupérer un fonctionalité publiée par un autre utilisateur :

`git flow feature pull origin {{feature}}`
