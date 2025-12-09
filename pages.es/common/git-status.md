# git status

> Muestra los cambios realizados en los archivos del repositorio Git.
> Lista los archivos cambiados, añadidos y eliminados comparándolos con la confirmación (commit) actual.
> Más información: <https://git-scm.com/docs/git-status>.

- Muestra los archivos modificados que aún no se han añadido para hacer una confirmación (commit):

`git status`

- Muestra la salida en formato breve:

`git status {{[-s|--short]}}`

- Muestra información detallada sobre cambios tanto en el área de preparación (staging) como en el directorio de trabajo:

`git status {{[-vv|--verbose --verbose]}}`

- Muestra la rama (branch) e información de seguimiento:

`git status --branch`

- Muestra la salida en formato breve junto a la información de la rama (branch):

`git status {{[-sb|--short --branch]}}`

- Muestra el número de entradas en rama temporal (stash):

`git status --show-stash`

- Muestra los archivos rastreados, excluyendo los no rastreados (untracked):

`git status {{[-uno|--untracked-files=no]}}`
