# git send-email

> Envoyer une collection de correctifs par email.
> Les correctifs peuvent être spécifiés sous forme de fichiers, de directions ou de liste de révisions.
> Plus d'informations : <https://git-scm.com/docs/git-send-email>.

- Envoyer le dernier commit de la branche courrante :

`git send-email -1`

- envoyer un commit spécifiaue :

`git send-email -1 {{commit}}`

- envoyer de multiples commits de la branche courrante (ici : 10) :

`git send-email {{-10}}`

- Envoyez un e-mail de présentation de la série de correctifs :

`git send-email -{{number of commits}} --compose`

- Consultez et modifiez l'e-mail de chaque patch que vous êtes sur le point d'envoyer :

`git send-email -{{number of commits}} --annotate`
