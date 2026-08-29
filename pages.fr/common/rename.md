# rename

> Renomme un fichier ou un groupe de fichiers à l’aide d’une `regex`.
> AVERTISSEMENT : cette commande remplacera les fichiers sans demander de confirmation, sauf si l’option de simulation est utilisée.
> Remarque : cette page concerne la version Perl, également appelée `file-rename`.
> Plus d'informations : <https://manned.org/prename>.

- Remplace `from` par `to` dans les noms des fichiers spécifiés :

`rename 's/{{from}}/{{to}}/' {{*.txt}}`

- Effectue une simulation — affiche les modifications qui seraient effectuées sans les appliquer :

`rename -n 's/{{from}}/{{to}}/' {{*.txt}}`

- Modifie l’extension :

`rename 's/\.{{old}}$/\.{{new}}/' {{*.txt}}`

- Convertit les noms en minuscules (utilise `-f` avec les systèmes de fichiers insensibles à la casse) :

`rename {{[-f|--force]}} 'y/A-Z/a-z/' {{*.txt}}`

- Met en majuscule la première lettre de chaque mot du nom :

`rename {{[-f|--force]}} 's/\b(\w)/\U$1/g' {{*.txt}}`

- Remplace les espaces par des underscores :

`rename 's/\s+/_/g' {{*.txt}}`
