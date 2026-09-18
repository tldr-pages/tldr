# git am

> Applique des fichiers de "patch" Git. Utile lorsque l'on reçoit des validations par email.
> Voir aussi : `git format-patch`.
> Plus d'informations : <https://git-scm.com/docs/git-am>.

- Applique un fichier de patch :

`git am {{chemin/vers/fichier.patch}}`

- Annule l'application d'un fichier de patch :

`git am --abort`

- Applique autant de fichiers de correctif que possible, en enregistrant les morceaux échoués pour rejeter le fichier :

`git am --reject {{chemin/vers/fichier.patch}}`
