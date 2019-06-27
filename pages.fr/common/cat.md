# cat

> Affiche et concatène le contenu d'un ou plusieurs fichiers.

- Affiche le contenu d'un fichier sur la sortie standard:

`cat {{file}}`

- Concatène le contenu de plusieurs fichiers vers le fichier de destination:

`cat {{file1}} {{file2}} > {{target_file}}`

- Ajoute le contenu d'un ficher à la fin du fichier de destination:

`cat {{file1}} {{file2}} >> {{target_file}}`

- Numérote toutes les lignes affichées:

`cat -n {{file}}`
