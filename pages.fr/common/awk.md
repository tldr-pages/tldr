# awk

> Langage de programmation polyvalent pour travailler sur des fichiers.
> Remarque : Differentes implementations d'AWK font souvent de ceci un lien symbolique vers leur binaire
> Voir aussi : `gawk`.
> Plus d'informations : <https://github.com/onetrueawk/awk>.

- Affiche la cinquième colonne (ou le champ) dans un fichier qui utilise des espaces comme séparateur :

`awk '{print $5}' {{chemin/vers/fichier}}`

- Affiche la deuxième colonne des lignes contenant "string1" dans un fichier qui utilise des espaces comme séparateur :

`awk '/{{string1}}/ {print $2}' {{chemin/vers/fichier}}`

- Affiche la dernière colonne de chaque ligne d'un fichier en utilisant une virgule (au lieu des espaces) comme séparateur :

`awk -F ',' '{print $NF}' {{chemin/vers/fichier}}`

- Additionne les valeurs de la première colonne des lignes d'un fichier et affiche le total :

`awk '{s+=$1} END {print s}' {{chemin/vers/fichier}}`

- Affiche une ligne sur trois en partant de la première ligne :

`awk 'NR%3==1' {{chemin/vers/fichier}}`

- Affiche differents valeurs selon des conditions :

`awk '{if ($1 == "string1") print "Correspondance exacte string1"; else if ($1 ~ "string2") print "Correspondance partielle string2"; else print "string3"}' {{chemin/vers/fichier}}`

- Affiche les lignes dont la valeur de la 10ème colonne est comprise entre un min et un max :

`awk '($10 >= {{valeur_min}} && $10 <= {{valeur_max}})' {{chemin/vers/fichier}}`

- Affiche une table des utilisateurs avec un UID >= 1000, avec un en-tête et une sortie formatée, en utilisant les deux-points comme séparateur (%-20ssignifie : 20 caractères de chaîne alignés à gauche,%6s signifie : 6 caractères de chaîne alignés à droite) :

`awk 'BEGIN {FS=":";printf "%-20s %6s %25s\n", "Name", "UID", "Shell"} $4 >= 1000 {printf "%-20s %6d %25s\n", $1, $4, $7}' /etc/passwd`
