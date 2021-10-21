# git push

> Pousse les commits vers un dépôt distant.
> Plus d'informations : <https://git-scm.com/docs/git-push>.

- Envoie les changements locaux dans la branche courante vers sa contrepartie distante :

`git push`

- Envoie les changements locaux d'une branche spécifique vers sa contrepartie distante :

`git push {{nom_distant}} {{local_branch}}`

- Publie la branche courante vers un dépôt distant, crée le nom de la branche distante :

`git push {{nom_distant}} -u {{branche_distante}}`

- Envoi les changements locaux sur toutes les branches locales vers leur contrepartie sur le dépôt distant :

`git push --all {{nom_distant}}`

- Supprime une branche dans un dépôt distant :

`git push {{nom_distant}} --delete {{branche_distante}}`

- Supprime les branches distantes qui n'ont pas de contrepartie locale :

`git push --prune {{nom_distant}}`

- Publie les tags qui ne sont pas sur le dépôt distant :

`git push --tags`
