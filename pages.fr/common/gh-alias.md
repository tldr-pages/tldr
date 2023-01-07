# gh alias

> Gérer les alias de commandes GitHub CLI depuis la ligne de commande.
> Plus d'informations : <https://cli.github.com/manual/gh_alias>.

- Affiche l'aide pour la sous-commande `alias` :

`gh alias`

- Liste tous les alias pour lesquels `gh` est configuré :

`gh alias list`

- Crée un alias de sous-commande pour `gh` :

`gh alias set {{alias}} '{{commande_gh}}`

- Définit une commande shell comme sous-commande de `gh` :

`gh alias set --shell {{nom_de_l'alias}} {{commande}}`

- Supprime un alias :

`gh alias delete {{nom_de_l'alias}}`
