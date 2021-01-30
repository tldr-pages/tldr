# git am

> Appliaquer des fichiers de path. Utile lorsque l on recoit des comits par email.
> Voir aussi `git format-patch`, pour generer des ficheirs de patch.
> Plus d'informations : <https://git-scm.com/docs/git-am>.

- Appliquer un fichier de patch :

`git am {{chemin/vers/fichier.patch}}`

- Annuler l'application d un fichier de patch :

`git am --abort`

- Appliquer autant de fichier de correctif que possible, en enregistrant les morceaux échoués pour rejeter le fichier :

`git am --reject {{chemin/vers/fichier.patch}}`
