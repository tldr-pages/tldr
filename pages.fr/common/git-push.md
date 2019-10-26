# git push

> Pousse les commits vers un repository distant.
> Plus d'informations: <https://git-scm.com/docs/git-push>.

- Envoi les changements locaux dans la branch courante vers sa contrepartie distante :

`git push`

- Envoi les changements locaux d'une branche spécifique vers sa contrepartie distante :

`git push {{remote_name}} {{local_branch}}`

- Publie la branche courante vers un repository distants, crée le nom de la branche distante :

`git push {{remote_name}} -u {{remote_branch}}`

- Envoi les changements locaux sur toutes les branches locales vers leur contrepartie sur le repository distant :

`git push --all {{remote_name}}`

- Supprime une branche dans repository distant :

`git push {{remote_name}} --delete {{remote_branch}}`

- Supprime les branches distantes qui n'ont pas de contrepartie local :

`git push --prune {{remote_name}}`

- Publie les tags qui ne sont pas sur le repository distant :

`git push --tags`
