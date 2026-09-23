# git mv

> Déplace ou renomme des fichiers inscrits dans l'index.
> Plus d'informations : <https://git-scm.com/docs/git-mv>.

- Déplace les fichiers dans l'index Git, valide à la prochaine validation :

`git mv {{chemin/vers/fichier}} {{nouveau/chemin/vers/fichier}}`

- Renome un fichier et met à jour l'index, valide à la prochaine validation :

`git mv {{nom_fichier}} {{nouveau_nom_fichier}}`

- Force l'écrasement d'un fichier :

`git mv {{[-f|--force]}} {{fichier}} {{cible}}`
