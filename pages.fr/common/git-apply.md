# git apply

> Applique un correctif à un fichier et/ou à l index.
> Plus d'informations : <https://git-scm.com/docs/git-apply>.

- Afficher les messages à propos des fichiers corrigés :

`git apply --verbose {{chemin/vers/fichier}}`

- Applique le correctif et ajoute les fichiers à l index :

`git apply --index {{chemin/vers/fichier}}`

- Applique un correctif depuis une source distante :

`curl {{https://example.com/file.patch}} | git apply`

- Affiche les différences résultantes et applique le correctif :

`git apply --stat --apply {{chemin/vers/fichier}}`

- Applique le correctif en ordre inverse :

`git apply --reverse {{chemin/vers/fichier}}`

- Stocke le résultat du correctif dans l'index sans modifier la branche courante :

`git apply --cache {{chemin/vers/fichier}}`
