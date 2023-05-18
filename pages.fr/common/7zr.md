# 7zr

> Un archiveur de fichiers avec un haut taux de compression.
> Similaire à `7z` sauf qu'il supporte que les fichiers `.7z`.
> Plus d'informations : <https://manned.org/7zr>.

- Compresse un fichier ou un dossier :

`7zr a {{chemin/vers/archive.7z}} {{chemin/vers/le/fichier_ou_dossier}}`

- Chiffre une archive existante (en incluant les en-têtes) :

`7zr a {{chemin/vers/archive_chiffree.7z}} -p{{password}} -mhe={{on}} {{chemin/vers/archive.7z}}`

- Extrait une archive en conservant l'arborescence des fichiers :

`7zr x {{chemin/vers/archive.7z}}`

- Extrait une archive vers un dossier specifique :

`7zr x {{chemin/vers/archive.7z}} -o{{chemin/vers/la/sortie}}`

- Extrait une archive vers sortie standard :

`7zr x {{chemin/vers/archive.7z}} -so`

- Liste le contenu d'une archive :

`7zr l {{chemin/vers/archive.7z}}`

- Liste les types de compression disponible :

`7zr i`
