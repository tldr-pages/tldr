# afconvert

> Convertir entre les formats de fichiers AFF et brut.
> Plus d'information: <https://manned.org/afconvert.1>.

- Utiliser une extension spécifique (par défaut: `aff`):

`afconvert -a {{extension}} {{path/to/input_file}} {{path/to/output_file1 path/to/output_file2 ...}}`

- Utiliser un niveau de compression spécifique (par défaut: `7`):

`afconvert -X{{0..7}} {{path/to/input_file}} {{path/to/output_file1 path/to/output_file2 ...}}`
