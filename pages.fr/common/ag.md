# ag

> The Silver Searcher. Comme `ack`, mais inspire à être plus rapide.
> Plus d'informations : <https://manned.org/ag>.

- Trouve les fichiers qui contiennent `string`, et affiche les lignes correspondantes dans le contexte courant :

`ag string`

- Trouve les fichiers qui contiennent `string` dans un dossier spécifique :

`ag string {{chemin/vers/dossier}}`

- Trouve les fichiers qui contiennent `string`, mais affiche uniquement les noms des fichiers :

`ag {{[-l|--files-with-matches]}} string`

- Trouve les fichiers qui contiennent `STRING` en étant insensible à la casse et affiche que le résultat plutôt que la ligne entière :

`ag {{[-i|--ignore-case]}} {{[-o|--only-matching]}} STRING`

- Trouve `string` dans les fichiers nommés `nom_fichier` :

`ag string {{[-G|--file-search-regex]}} {{nom_fichier}}`

- Trouve des fichiers dont le contenu correspond à une `regex` :

`ag '{{^ca(t|r)$}}'`

- Trouve les fichiers avec un nom correspondant à `string` :

`ag {{[-g|--filename-pattern]}} string`
