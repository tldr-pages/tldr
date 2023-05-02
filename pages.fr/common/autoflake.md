# autoflake

> Un outil pour enlever les imports et les variables inutilisés d'un code Python.
> Plus d'informations : <https://github.com/myint/autoflake>.

- Enlève les variables non-utilisées d'un fichier et affiche la différence :

`autoflake --remove-unused-variables {{chemin/vers/fichier.py}}`

- Enlève les imports non-utilisés de plusieurs fichiers et affiche la différence :

`autoflake --remove-all-unused-imports {{chemin/vers/fichier1.py chemin/vers/fichier2.py ...}}`

- Enlève les variables non-utilisées d'un fichier, surcharge ce dernier :

`autoflake --remove-unused-variables --in-place {{chemin/vers/fichier.py}}`

- Enlève les variables non-utilisées de tous les fichiers d'un dossier de manière récursive, en les surchargeant :

`autoflake --remove-unused-variables --in-place --recursive {{chemin/vers/dossier}}`
