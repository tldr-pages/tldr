# git push

> Pousse les validations vers un dépôt distant.
> Plus d'informations : <https://git-scm.com/docs/git-push>.

- Envoie les modifications locales dans la branche actuelle vers sa contrepartie distante :

`git push`

- Envoie les modifications locales d'une branche spécifique vers sa contrepartie distante :

`git push {{nom_distant}} {{branche_locale}}`

- Envoie les modifications d'une branche locale spécifique vers sa contrepartie distante et définit cette dernière comme cible par défaut pour les opérations push/pull de la branche locale :

`git push {{[-u|--set-upstream]}} {{nom_distant}} {{branche_locale}}`

- Envoie les modifications d'une branche locale spécifique vers une branche distante spécifique :

`git push {{nom_distant}} {{branche_locale}}:{{branche_distante}}`

- Envoie les modifications locales sur toutes les branches locales vers leur contrepartie sur le dépôt distant :

`git push --all {{remote_name}}`

- Supprime une branche dans un dépôt distant :

`git push {{nom_distant}} {{[-d|--delete]}} {{branche_distante}}`

- Supprime les branches distantes qui n'ont pas de contrepartie locale :

`git push --prune {{nom_distant}}`

- Publie les tags qui ne sont pas encore sur le dépôt distant :

`git push --tags`
