# grep

> Recherche des motifs dans un texte.
> Supportes des motifs simple et des expressions rationnelles.

- Recherche une chaîne de caractères précise :

`grep {{search_string}} {{chemin/vers/fichier}}`

- Recherche en ignorant les distinctions de casse :

`grep -i {{search_string}} {{chemin/vers/fichier}}`

- Recherche récursivement (en ignorant les fichiers non-texte) dans le dossier courant une chaîne de caractères précise :

`grep -RI {{search_string}} .`

- Utilise des expressions rationnelles étendues (supporte `?`, `+`, `{}`, `()` et `|`) :

`grep -E {{^regex$}} {{chemin/vers/fichier}}`

- Affiche 3 lignes de [C]ontext autour, avant ([B]efore), ou [A]près chaque concordance :

`grep -{{C|B|A}} 3 {{search_string}} {{chemin/vers/fichier}}`

- Affiche le nom du fichier avec la ligne correspondante pour chaque concordance :

`grep -Hn {{search_string}} {{chemin/vers/fichier}}`

- Utilise l'entrée standard au lieu d'un fichier :

`cat {{chemin/vers/fichier}} | grep {{search_string}}`

- Inverse le résultat pour exclure des chaînes de caractères spécifique :

`grep -v {{search_string}}`
