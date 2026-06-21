# exiftool

> Lit et écrit les métadonnées dans des fichiers.
> Plus d'informations : <https://exiftool.org/exiftool_pod.html>.

- Affiche les métadonnées EXIF d'un fichier donné :

`exiftool {{chemin/vers/le/fichier}}`

- Supprime toutes les métadonnées EXIF des fichiers donnés :

`exiftool -All= {{chemin/vers/fichier1 chemin/vers/fichier2 ...}}`

- Supprime les métadonnées EXIF GPS des fichiers image donnés :

`exiftool "-gps*=" {{chemin/vers/image1 chemin/vers/image2 ...}}`

- Supprime toutes les métadonnées EXIF des fichiers image donnés, puis ré-ajoute les métadonnées de couleur et d'orientation :

`exiftool -All= -tagsfromfile @ -colorspacetags -orientation {{chemin/vers/image1 chemin/vers/image2 ...}}`

- Avance d'une heure la date de prise de toutes les photos d'un répertoire :

`exiftool "-AllDates+=0:0:0 1:0:0" {{chemin/vers/le/répertoire}}`

- Recule d'un jour et deux heures la date de prise de toutes les photos JPEG du répertoire courant :

`exiftool "-AllDates-=0:0:1 2:0:0" {{[-ext|-extension]}} jpg`

- Modifie uniquement le champ `DateTimeOriginal` en soustrayant 1,5 heure, sans conserver de sauvegardes :

`exiftool -DateTimeOriginal-=1.5 -overwrite_original`

- Renomme récursivement toutes les photos JPEG d'un répertoire à partir du champ `DateTimeOriginal` :

`exiftool '-filename<DateTimeOriginal' {{[-d|-dateFormat]}} %Y-%m-%d_%H-%M-%S%%lc.%%e {{chemin/vers/le/répertoire}} {{[-r|-recurse]}} {{[-ext|-extension]}} jpg`
