# ag

> The Silver Searcher. Comme `ack`, mais inspire à être plus rapide.
> Plus d'informations : <https://github.com/ggreer/the_silver_searcher>.

- Trouve les fichiers qui contiennent "foo", et affiche les lignes correspondantes dans le contexte courant :

`ag {{foo}}`

- Trouve les fichiers qui contiennent "foo" dans un dossier spécifique :

`ag {{foo}} {{chelin/vers/dossier}}`

- Trouve les fichiers qui contiennent "foo", mais affiche les nom de fichier uniquement :

`ag -l {{foo}}`

- Trouve les fichiers qui contiennent "FOO" en étant insensible à la casse et affiche que le premier résultat plutôt que la ligne entière :

`ag -i -o {{FOO}}`

- Trouve "foo" dans les fichiers avec un nom contenant "bar" :

`ag {{foo}} -G {{bar}}`

- Trouve des fichiers dont le contenu correspond à une expression régulière :

`ag '{{^ba(r|z)$}}'`

- Trouve les fichiers avec un nom contenant "foo" :

`ag -g {{foo}}`
