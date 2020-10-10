# git branch

> Commande git principale pour travailler avec des branches.
> Plus d'informations: <https://git-scm.com/docs/git-branch>.

- Liste les branches locale, prefixe la branche courrante avec `*`:

`git branch`

- Liste toutes les branches (locale et distantes):

`git branch -a`

- Affiche le nom de la branche courrante:

`git branch --show-current`

- Crée une nouvelle branche depuis le commit courrant:

`git branch {{branch_name}}`

- Crée une nouvelle branche depuis un commit en particulier:

`git branch {{branch_name}} {{commit_hash}}`

- Renommer une branche (ne pas se trouver sur la branche pour le faire):

`git branch -m {{old_branch_name}} {{new_branch_name}}`

- Supprimer un branche locale (ne pas se trouver sur la branche pour le faire):

`git branch -d {{branch_name}}`

- Supprimer une branche distante:

`git push {{remote_name}} --delete {{remote_branch_name}}`
