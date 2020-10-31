# git stash

> Stocker les modifications Git locales dans une zone temporaire.
> Plus d'informations: <https://git-scm.com/docs/git-stash>.

- Stocker les changements courrants, sauf les fichiers non suivis :

`git stash [push -m {{optional_stash_message}}]`

- Stocker les changements courrants, incluant le sfichiers non suivis :

`git stash -u`

- Stocker les parties d'un fichier interactivement :

`git stash -p`

- Lister tout les stash (saffiche leurs noms, les branches relatives et messages) :

`git stash list`

- Applique un stash (par défaut, le dernier, nommé stash@{0}) :

`git stash apply {{optional_stash_name_or_commit}}`

- Applique un stash (par défaut le dernier, stash@{0}), et le suprimmer de la liste des stash si il n'y a pas de conflits :

`git stash pop {{optional_stash_name}}`

- Suprime un stash (par défaut le dernier, stash@{0}) :

`git stash drop {{optional_stash_name}}`

- Suprime tout les stash:

`git stash clear`
