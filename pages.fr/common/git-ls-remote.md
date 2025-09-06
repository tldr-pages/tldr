# git ls-remote

> Commande Git pour répertorier les références dans un dépôt distant en fonction du nom ou de l'URL.
> Si aucun nom ou URL n'est donné, alors la branche amont configurée sera utilisée, ou l'origine distante si la première n'est pas configurée.
> Plus d'informations : <https://git-scm.com/docs/git-ls-remote>.

- Afficher les références du dépôt configuré par défaut :

`git ls-remote`

- Afficher uniquement les références HEAD du dépôt configuré par défaut :

`git ls-remote --heads`

- Afficher uniquement les tags du dépôt configuré par défaut :

`git ls-remote --tags`

- Afficher les références du dépôt précisé :

`git ls-remote {{url-du-dépôt}}`

- Afficher les références du dépôt précisé filtrés par un motif :

`git ls-remote {{nom-du-dépôt}} "{{motif}}"`
