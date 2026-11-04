# zoxide

> Garde une trace des répertoires les plus utilisés.
> Utilise un algorithme de classement pour accéder au meilleur résultat.
> Plus d'informations : <https://manned.org/zoxide>.

- Accède au répertoire avec le meilleur classement qui contient "string" dans son nom :

`zoxide query string`

- Accède au répertoire avec le meilleur classement qui contient "string1" puis "string2" dans son nom :

`zoxide query string1 string2`

- Démarre une recherche de répertoire interactive (nécessite `fzf`) :

`zoxide query {{[-i|--interactive]}}`

- Ajoute un répertoire ou incrémente son classement :

`zoxide add {{chemin/vers/répertoire}}`

- Supprime un répertoire de la base de données de `zoxide` :

`zoxide remove {{chemin/vers/répertoire}}`

- Génère la configuration du shell pour la mise en place des alias de commandes (`z`, `zi`) :

`zoxide init {{bash|elvish|fish|nushell|posix|powershell|tcsh|xonsh|zsh}}`
