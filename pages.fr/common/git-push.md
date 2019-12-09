# git push

> Pousse les commits vers un dépôt distant.
> Plus d'informations: <https://git-scm.com/docs/git-push>.

- Envoie les changements locaux dans la branch courante vers sa contrepartie distante :

`git push`

- Envoie les changements locaux d'une branche spécifique vers sa contrepartie distante :

`git push {{remote_name}} {{local_branch}}`

- Publie la branche courante vers un dépôt distant, crée le nom de la branche distante :

`git push {{remote_name}} -u {{remote_branch}}`

- Envoi les changements locaux sur toutes les branches locales vers leur contrepartie sur le dépôt distant :

`git push --all {{remote_name}}`

- Supprime une branche dans un dépôt distant :

`git push {{remote_name}} --delete {{remote_branch}}`

- Supprime les branches distantes qui n'ont pas de contrepartie locale :

`git push --prune {{remote_name}}`

- Publie les tags qui ne sont pas sur le dépôt distant :

`git push --tags`
