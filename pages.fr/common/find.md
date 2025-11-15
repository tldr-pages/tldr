# find

> Trouve récursivement des fichiers ou des dossiers dans l'arborescence spécifiée.
> Plus d'informations : <https://manned.org/find>.

- Trouve des fichiers par extension :

`find {{racine}} -name '{{*.ext}}'`

- Trouve des fichiers correspondant à plusieurs chemins ou motifs :

`find {{racine}} -path '{{**/chemin/**/*.ext}}' -or -name '{{*motif*}}'`

- Trouve des dossiers correspondant à un nom donné sans vérifier la casse :

`find {{racine}} -type d -iname '{{*lib*}}'`

- Trouve des fichiers correspondant à un motif donné en excluant certains chemins de la recherche :

`find {{racine}} -name '{{*.py}}' -not -path '{{*/site-packages/*}}'`

- Trouve des fichiers dans une fourchette de tailles et limite la profondeur récursive à "1" :

`find {{racine}} -maxdepth 1 -size {{+500k}} -size {{-10M}}`

- Exécute une commande pour chaque fichier (utiliser `{}` dans la commande pour utiliser le nom des fichiers) :

`find {{racine}} -name '{{*.ext}}' -exec {{wc -l {} }}\;`

- Trouve les fichiers modifiés dans les 7 derniers jours :

`find {{racine}} -daystart -mtime -{{7}}`

- Trouve les fichiers vides (de taille nulle) et les supprimer :

`find {{racine}} -type {{f}} -empty -delete`
