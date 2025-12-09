# git restore

> Restaurez les fichiers de l'arborescence de travail. Nécessite la version 2.23+ de Git.
> Voir aussi `git checkout`.
> Plus d'informations : <https://git-scm.com/docs/git-restore>.

- Restaurer un fichier supprimé à partir du contenu du commit actuel (HEAD) :

`git restore {{chemin/vers/fichier}}`

- Restaurer un fichier a la version d'un commit spécifié :

`git restore --source {{commit}} {{chemin/vers/fichier}}`

- Annulez toutes les modifications non validées des fichiers suivis, en revenant au HEAD :

`git restore .`
