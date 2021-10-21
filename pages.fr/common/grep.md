# grep

> Recherche des motifs dans un texte.
> Supporte des motifs simples et des expressions régulières.
> Plus d'informations : <https://www.gnu.org/software/grep/manual/grep.html>.

- Recherche une chaîne de caractères précise :

`grep {{chaîne_recherchée}} {{chemin/vers/fichier}}`

- Recherche en ignorant la casse :

`grep -i {{chaîne_recherchée}} {{chemin/vers/fichier}}`

- Recherche récursivement (en ignorant les fichiers non-texte) dans le dossier courant une chaîne de caractères précise :

`grep -RI {{chaîne_recherchée}} .`

- Utilise des expressions régulières étendues (supporte `?`, `+`, `{}`, `()` et `|`) :

`grep -E {{expression_régulière}} {{chemin/vers/fichier}}`

- Affiche 3 lignes de [C]ontexte, avant ([B]efore), ou [A]près chaque concordance :

`grep -{{C|B|A}} 3 {{chaîne_recherchée}} {{chemin/vers/fichier}}`

- Affiche le nom du fichier avec la ligne correspondante pour chaque concordance :

`grep -Hn {{chaîne_recherchée}} {{chemin/vers/fichier}}`

- Utilise l'entrée standard au lieu d'un fichier :

`cat {{chemin/vers/fichier}} | grep {{chaîne_recherchée}}`

- Inverse le résultat pour exclure des chaînes de caractères spécifiques :

`grep -v {{chaîne_recherchée}}`
