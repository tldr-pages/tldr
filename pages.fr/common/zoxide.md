# zoxide

> Garde une trace des répertoires les plus utilisés.
> Utilise un algorithme de classement pour identifier le meilleur résultat.
> Plus d'informations : <https://github.com/ajeetdsouza/zoxide>.

- Aller au répertoire avec le meilleur classement qui contient "foo" dans son nom :

`zoxide query {{foo}}`

- Aller au répertoire avec le meilleur classement qui contient "foo" et "bar" dans son nom :

`zoxide query {{foo}} {{bar}}`

- Démarre une recherche de répertoire interactive (nécessite `fzf`) :

`zoxide query --interactive`

- Ajoute un répertoire ou incrémente son classement :

`zoxide add {{chemin/du/répertoire}}`

- Supprime un répertoire de la base de données de `zoxide` :

`zoxide remove {{chemin/du/répertoire}}`

- Génère la configuration du shell pour la mise en place des alias de commandes (`z`, `za`, `zi`, `zq`, `zr`) :

`zoxide init {{bash|fish|zsh}}`
