# git ls-remote

> Commande Git pour répertorier les références dans un dépot distant en fonction du nom ou de l'URL.
> Si aucun nom ou URL n'est donné, alors la branche amont configurée sera utilisée, ou l'origine distante si la première n'est pas configurée.
> Plus d'informations : <https://git-scm.com/docs/git-ls-remote>.

- Afficher les références du dépot configuré par défaut :

`git ls-remote`

- Afficher uniquement les références HEAD du dépot configuré par défaut :

`git ls-remote --heads`

- Afficher uniquement les tags du dépot configuré par défaut :

`git ls-remote --tags`

- Afficher les références du dépot précisé :

`git ls-remote {{repositiory-url}}`

- Afficher les références du dépot précisé filtrés par un pattern :

`git ls-remote {{repositiory-name}} "{{pattern}}"`
