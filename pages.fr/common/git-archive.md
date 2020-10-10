# git archive

> Cree une archive de fichiers depuis un branche donée.
> Plus d informations: <https://git-scm.com/docs/git-archive>.

- Crée une archive .tar avec le contenu de la HEAD et l'affiche sur la sortie stanard:

`git archive --verbose HEAD`

- Crée une archive .zip avec le contenu de la HEAD et l'affiche sur la sortie stanard:

`git archive --verbose --format=zip HEAD`

- Pareil que ci-dessus mais ecrit dans l archive specifiée:

`git archive --verbose --output={{path/to/file.zip}} HEAD`

- Crée une archive depuis le dernier commit de la branche spécifiée:

`git archive --output={{path/to/file.tar}} {{branch_name}}`

- Crée une archive avec le contenu d un repertoire donné:

`git archive --output={{path/to/file.tar}} HEAD:{{path/to/directory}}`

- Ajoutez un chemin d'accès à chaque fichier pour l'archiver dans un répertoire spécifique:

`git archive --output={{path/to/file.tar}} --prefix={{path/to/prepend}}/ HEAD`
