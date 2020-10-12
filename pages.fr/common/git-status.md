# git status

> Afficher les changements aux fichier d'un dépôt Git.
> Les fichiers changés, ajoutés et supprimés seront comparés au commit où se situe la tête.
> Plus d'informations: <https://git-scm.com/docs/git-status>.

- Afficher les fichiers changés qui n'ont pas été ajouté dans le *stage*:

`git status`

- Afficher le résultat de façon conci[s]e:

`git status -s`

- Afficher seulement les changements de fichiers suivi:

`git status --untracked-files=no`

- Montrer le résultat de façon conci[s]e avec de l'information sur la [b]ranche:

`git status -sb`
