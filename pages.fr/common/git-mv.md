# git mv

> Déplace ou renomme des fichiers et met à jour l'index Git.
> Plus d'informations : <https://git-scm.com/docs/git-mv>.

- Déplace un fichier dans le dépôt et ajoute le déplacement à la prochaine validation :

`git mv {{chemin/vers/fichier}} {{chemin/vers/destination}}`

- Renomme un fichier ou un répertoire et ajoute le renommage à la prochaine validation :

`git mv {{chemin/vers/fichier_ou_répertoire}} {{chemin/vers/destination}}`

- Écrase le fichier ou le répertoire situé dans le chemin de destination s’il existe déjà :

`git mv {{[-f|--force]}} {{chemin/vers/fichier_ou_répertoire}} {{chemin/vers/destination}}`
