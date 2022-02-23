# egrep

> Recherche de motifs dans un texte. Supporte la version étendues des expressions regulieres (`?`, `+`, `{}`, `()`, et `|`).
> Plus d'informations : <https://manned.org/egrep>.

- Recherche une chaîne de caractères précise :

`egrep "{{chaîne_recherchée}}" {{chemin/vers/fichier}}`

- Recherche une chaîne de caractères dans plusieurs fichiers :

`egrep "{{chaîne_recherchée}}" {{chemin/vers/fichier1}} {{chemin/vers/fichier2}} {{chemin/vers/fichier3}}`

- Utilise l'entrée standard au lieu d'un fichier :

`cat {{chemin/vers/fichier}} | egrep {{chaîne_recherchée}}`

- Affiche le nom du fichier avec la ligne correspondante pour chaque concordance :

`egrep --with-filename --line-number "{{chaîne_recherchée}}" {{chemin/vers/fichier}}`

- Recherche récursivement dans le dossier courant, en ignorant les fichiers binaires, une chaîne de caractères précise :

`egrep --recursive --binary-files={{without-match}} "{{chaîne_recherchée}}" {{chemin/vers/fichier}}`

- Inverse le résultat pour exclure des chaînes de caractères spécifiques :

`egrep --invert-match "{{chaîne_recherchée}}" {{chemin/vers/fichier}}`
