# git add

> Añade los archivos cambiados al índice.
> Más información: <https://git-scm.com/docs/git-add>.

- Añade un archivo al índice:

`git add {{ruta/al/archivo}}`

- Añade todos los archivos (rastreados o no):

`git add {{[-A|--all]}}`

- Añade todos los archivos en el directorio actual:

`git add .`

- Añade únicamente los archivos ya rastreados:

`git add {{[-u|--update]}}`

- Añade también los archivos ignorados:

`git add {{[-f|--force]}}`

- Añade interactivamente partes de archivos al área de preparación (staging):

`git add {{[-p|--patch]}}`

- Añade interactivamente partes de un archivo dado al área de preparación (staging):

`git add {{[-p|--patch]}} {{ruta/al/archivo}}`

- Añade un archivo interactivamente al área de preparación (staging):

`git add {{[-i|--interactive]}}`
