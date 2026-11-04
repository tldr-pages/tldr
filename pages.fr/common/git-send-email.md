# git send-email

> Envoie une collection de correctifs par email.
> Les correctifs peuvent être spécifiés sous forme de fichiers, de directions ou de liste de révisions.
> Plus d'informations : <https://git-scm.com/docs/git-send-email>.

- Envoie la dernière validation de la branche actuelle :

`git send-email -1`

- Envoie une validation spécifique :

`git send-email -1 {{validation}}`

- Envoie de multiples validations de la branche actuelle (ici : 10) :

`git send-email {{-10}}`

- Envoie un e-mail de présentation de la série de correctifs :

`git send-email -{{nombre_validations}} --compose`

- Consulte et modifie l'e-mail de chaque correctif qui va être envoyé :

`git send-email -{{nombre_validations}} --annotate`
