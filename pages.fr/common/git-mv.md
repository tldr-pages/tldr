# git mv

> Déplacer ou renommer des fichiers inscrits dans l'index.
> Plus d'informations : <https://git-scm.com/docs/git-mv>.

- Déplace les fichiers dans l'index Git, valide au prochain commit :

`git mv {{chemin/vers/fichier}} {{new/path/to/file}}`

- Renome un fichier et met a jour l'index, valide au prochain commit :

`git mv {{filename}} {{new_filename}}`

- Force l'écrasement d'un fichier :

`git mv --force {{file}} {{cible}}`
