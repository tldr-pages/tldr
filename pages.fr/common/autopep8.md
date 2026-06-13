# autopep8

> Formate du code Python en accord avec le style PEP 8.
> Plus d'informations : <https://github.com/hhatto/autopep8>.

- Formate une fichier vers la sortie standard, avec une taille de ligne maximal personnalisée :

`autopep8 {{chemin/vers/fichier.py}} --max-line-length {{longueur}}`

- Formate un fichier, en affichant les changements :

`autopep8 --diff {{chemin/vers/fichier}}`

- Formate un fichier et sauvegarde les changements :

`autopep8 --in-place {{chemin/vers/fichier.py}}`

- Formate récursivement les fichiers dans un dossier et sauvegarde les changements :

`autopep8 --in-place --recursive {{chemin/vers/dossier}}`
