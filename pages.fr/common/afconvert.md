# afconvert

> Convertir entre les formats de fichiers AFF et brut.
> Plus d'informations : <https://manned.org/afconvert.1>.

- Utiliser une extension spécifique (par défaut: `aff`) :

`afconvert -a {{extension}} {{chemin/vers/fichier_source}} {{chemin/vers/fichier_de_sortie1 chemin/vers/fichier_de_sortie2 ...}}`

- Utiliser un niveau de compression spécifique (par défaut: `7`) :

`afconvert -X{{0..7}} {{chemin/vers/fichier_source}} {{chemin/vers/fichier_de_sortie1 chemin/vers/fichier_de_sortie2 ...}}`
