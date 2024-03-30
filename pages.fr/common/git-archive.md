# git archive

> Crée une archive de fichiers depuis un branche donnée.
> Plus d'informations : <https://git-scm.com/docs/git-archive>.

- Crée une archive `.tar` avec le contenu de la HEAD et l'affiche sur la sortie standard :

`git archive --verbose HEAD`

- Crée une archive Zip avec le contenu de la HEAD et l'affiche sur la sortie standard :

`git archive --verbose --format zip HEAD`

- Pareil que ci-dessus mais écrit dans l'archive spécifiée :

`git archive --verbose --output {{chemin/vers/fichier.zip}} HEAD`

- Crée une archive depuis le dernier commit de la branche spécifiée :

`git archive --output {{chemin/vers/fichier.tar}} {{nom_de_branche}}`

- Crée une archive avec le contenu d'un répertoire donné :

`git archive --output {{chemin/vers/fichier.tar}} HEAD:{{chemin/vers/repertoire}}`

- Ajoutez un chemin d'accès à chaque fichier pour l'archiver dans un répertoire spécifique :

`git archive --output {{chemin/vers/fichier.tar}} --prefix {{chemin/vers/cible}}/ HEAD`
