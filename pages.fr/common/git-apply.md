# git apply

> Applique un correctif a un fichier et/ou a l index.
> Plus d informations: <https://git-scm.com/docs/git-apply>.

- Afficher les messages a propos des fichiers corrigés:

`git apply --verbose {{path/to/file}}`

- Applique le correctif et ajoute les fichiers a l index:

`git apply --index {{path/to/file}}`

- Applique un correctif depuis une source distante:

`curl {{https://example.com/file.patch}} | git apply`

- Affiche les differencs resultantes et applique le correctif:

`git apply --stat --apply {{path/to/file}}`

- Applique le correctif en ordre inverse:

`git apply --reverse {{path/to/file}}`

- Stocke le resultat du correctif dans l index sans modifier la branche courrante:

`git apply --cache {{path/to/file}}`
