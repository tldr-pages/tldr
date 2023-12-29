# git stash

> Stocker les modifications Git locales dans une zone temporaire.
> Plus d'informations : <https://git-scm.com/docs/git-stash>.

- Stocker les changements courants, sauf les fichiers non-suivis :

`git stash push -m {{nom_de_stash_optionel}}`

- Stocker les changements courants, incluant les fichiers non-suivis :

`git stash -u`

- Stocker les parties d'un fichier interactivement :

`git stash -p`

- Lister tous les stashs (affiche leurs noms, les branches relatives et messages) :

`git stash list`

- Applique un stash (par défaut, le dernier, nommé stash@{0}) :

`git stash apply {{nom_de_stash_ou_de_commit_optionel}}`

- Applique un stash (par défaut le dernier, stash@{0}), et le supprimer de la liste des stashs s'il n'y a pas de conflit :

`git stash pop {{nom_de_stash_optionel}}`

- Supprime tous les stashs :

`git stash clear`
