# 7za

> Un archiveur de fichiers avec un haut taux de compression.
> Similaire à `7z` sauf qu'il supporte moins de type de fichiers mais il est multi-plateforme.
> Plus d'informations : <https://manned.org/7za>.

- Compresse un fichier ou un dossier :

`7za a {{chemin/vers/archive.7z}} {{chemin/vers/file_or_directory}}`

- Chiffre une archive existante (en incluant les en-têtes) :

`7za a {{chemin/vers/archive_chiffree.7z}} -p{{motdepasse}} -mhe=on {{chemin/vers/archive.7z}}`

- Extrait une archive en conservant l'arborescence des fichiers :

`7za x {{chemin/vers/archive.7z}}`

- Extrait une archive vers un dossier specifique :

`7za x {{chemin/vers/archive.7z}} -o{{chemin/vers/la/sortie}}`

- Extrait une archive vers sortie standard :

`7za x {{chemin/vers/archive.7z}} -so`

- Compresse en utilisant une compression spécifique :

`7za a -t{{7z|bzip2|gzip|lzip|tar|zip}} {{chemin/vers/archive.7z}} {{chemin/vers/le/fichier_ou_dossier}}`

- Liste le contenu d'une archive :

`7za l {{chemin/vers/archive.7z}}`
