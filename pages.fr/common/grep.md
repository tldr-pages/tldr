# grep

> Recherche des motifs dans un texte.
> Supporte des motifs simples et des expressions régulières.
> Plus d'informations : <https://www.gnu.org/software/grep/manual/grep.html>.

- Recherche une chaîne de caractères précise :

`grep "{{chaîne_recherchée}}" {{chemin/vers/fichier}}`

- Recherche en ignorant la casse :

`grep {{[-F|--fixed-strings]}} "{{chaîne_recherchée}}" {{chemin/vers/fichier}}`

- Recherche récursivement (en ignorant les fichiers non-texte) dans le dossier courant une chaîne de caractères précise :

`grep {{[-r|--recursive]}} {{[-n|--line-number]}} "{{chaîne_recherchée}}" .`

- Utilise des expressions régulières étendues (supporte `?`, `+`, `{}`, `()` et `|`) :

`grep {{[-Ei|--extended-regexp --ignore-case]}} {{expression_régulière}} {{chemin/vers/fichier}}`

- Affiche 3 lignes de [C]ontexte, avant ([B]efore), ou [A]près chaque concordance :

`grep {{--context|--before-context|--after-context}} 3 "{{chaîne_recherchée}}" {{chemin/vers/fichier}}`

- Affiche le nom du fichier avec la ligne correspondante pour chaque concordance :

`grep {{[-Hn|--with-filename --line-number]}} --color=always "{{chaîne_recherchée}}" {{chemin/vers/fichier}}`

- Utilise l'entrée standard au lieu d'un fichier :

`cat {{chemin/vers/fichier}} | grep "{{chaîne_recherchée}}"`
