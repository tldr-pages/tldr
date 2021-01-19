# git apply

> Applique un correctif a un fichier et/ou a l index.
> Plus d'informations : <https://git-scm.com/docs/git-apply>.

- Afficher les messages a propos des fichiers corrigés :

`git apply --verbose {{chemin/vers/fichier}}`

- Applique le correctif et ajoute les fichiers a l index :

`git apply --index {{chemin/vers/fichier}}`

- Applique un correctif depuis une source distante :

`curl {{https://example.com/file.patch}} | git apply`

- Affiche les differencs resultantes et applique le correctif :

`git apply --stat --apply {{chemin/vers/fichier}}`

- Applique le correctif en ordre inverse :

`git apply --reverse {{chemin/vers/fichier}}`

- Stocke le resultat du correctif dans l index sans modifier la branche courrante :

`git apply --cache {{chemin/vers/fichier}}`
