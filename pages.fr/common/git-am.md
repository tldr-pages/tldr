# git am

> Appliquer des fichiers de "patch" Git. Utile lorsque l'on reçoit des commits par email.
> Voir aussi `git format-patch`, pour générer des fichiers de patch.
> Plus d'informations : <https://git-scm.com/docs/git-am>.

- Appliquer un fichier de patch :

`git am {{chemin/vers/fichier.patch}}`

- Annuler l'application d'un fichier de patch :

`git am --abort`

- Appliquer autant de fichiers de correctif que possible, en enregistrant les morceaux échoués pour rejeter le fichier :

`git am --reject {{chemin/vers/fichier.patch}}`
