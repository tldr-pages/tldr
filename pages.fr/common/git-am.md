# git am

> Applique des fichiers de "patch" Git et crée une validation. Utile lorsque l'on reçoit des validations par email.
> Voir aussi : `git format-patch`.
> Plus d'informations : <https://git-scm.com/docs/git-am>.

- Applique et valide un fichier de patch local :

`git am {{chemin/vers/fichier.patch}}`

- Applique et valide un fichier de patch distant :

`curl {{[-L|--location]}} {{https://example.com/fichier.patch}} | git am`

- Annule l'application d'un fichier de patch :

`git am --abort`

- Applique autant que possible un fichier de patch, en enregistrant les morceaux qui échouent dans des fichiers de rejet :

`git am --reject {{chemin/vers/fichier.patch}}`
