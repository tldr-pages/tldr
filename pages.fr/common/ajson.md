# ajson

> Exécute un JSONPath sur un objet JSON.
> Plus d'informations : <https://github.com/spyzhov/ajson>.

- Lis un JSON depuis un fichier et exécute une expression JSONPath spécifique :

`ajson '{{$..json[?(@.path)]}}' {{chemin/vers/fichier.json}}`

- Lis un JSON depuis l'entrée standard et exécute une expression JSONPath spécifique :

`cat {{chemin/vers/fichier.json}} | ajson '{{$..json[?(@.path)]}}'`

- Lis un JSON depuis une URL et évalue une expression JSONPath spécifique :

`ajson '{{avg($..price)}}' '{{https://exemple.com/api/}}'`

- Lis un JSON simple et calcule une valeur :

`echo '{{3}}' | ajson '{{2 * pi * $}}'`
