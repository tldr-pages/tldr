# awk

> Langage de programmation polyvalent pour travailler sur des fichiers.
> Pour plus d'informations : <https://github.com/onetrueawk/awk>.

- Affiche la cinquième colonne (ou le champ) dans un fichier qui utilise des espaces comme séparateur :

`awk '{print $5}' {{nom_de_fichier}}`

- Affiche la deuxième colonne dans des lignes contenant "quelque-chose" dans un fichier qui utilise des espaces comme séparateur :

`awk '/{{quelque-chose}}/ {print $2}' {{nom_de_fichier}}`

- Affiche la dernière colonne de chaque ligne d'un fichier en utilisant une virgule (au lieu des espaces) comme séparateur :

`awk -F ',' '{print $NF}' {{nom_de_fichier}}`

- Additionne les valeurs de la première colonne des lignes d'un fichier et affiche le total :

`awk '{s+=$1} END {print s}' {{nom_de_fichier}}`

- Additionne les valeurs de la première colonne des lignes d'un fichier et affiche ces valeurs puis affiche le total :

`awk '{s+=$1; print $1} END {print "--------"; print s}' {{nom_de_fichier}}`

- Affiche une ligne sur trois en partant de la première ligne :

`awk 'NR%3==1' {{nom_de_fichier}}`
