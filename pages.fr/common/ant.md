# ant

> Apache Ant.
> Outil pour construire et gérer les projets basés sur du Java.
> Plus d'informations : <https://ant.apache.org>.

- Construit un projet avec le fichier de construction `build.xml` :

`ant`

- Construit un projet en utilisant un autre fichier que `build.xml` :

`ant -f {{fichier_de_construction.xml}}`

- Affiche les informations sur les cibles possibles pour ce projet :

`ant -p`

- Affiche les informations de débogage :

`ant -d`

- Exécute toutes les cibles qui ne dépendent pas d'une ou plusieurs cibles en erreur :

`ant -k`
