# chattr

> Modifie les attributs des fichiers ou des répertoires.
> Plus d'informations : <https://manned.org/chattr>.

- Rend un fichier ou un répertoire [i]mmuable aux modifications et à la suppression, même par le superutilisateur :

`sudo chattr +i {{chemin/vers/fichier_ou_répertoire}}`

- Rend un fichier ou un répertoire muable :

`sudo chattr -i {{chemin/vers/fichier_ou_répertoire}}`

- Rend [R]écursivement un répertoire entier et son contenu immuables :

`sudo chattr -R +i {{chemin/vers/répertoire}}`

- Indique qu'un répertoire et ses fichiers doivent être interprétés de manière insensible à la casse :

`chattr +F {{chemin/vers/répertoire}}`

- Configure un fichier pour qu'il n'autorise que l'[a]jout de données :

`sudo chattr +a {{chemin/vers/fichier}}`
