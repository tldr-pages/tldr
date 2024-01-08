# git diff

> Muestra los cambios de los archivos rastreados.
> Más información: <https://git-scm.com/docs/git-diff>.

- Muestra los cambios sin marcar ni commit:

`git diff`

- Muestra todos los cambios sin commit, pero incluye los marcados:

`git diff HEAD`

- Muestra solo los cambios marcados pero que no tienen commit:

`git diff --staged`

- Muestra los cambios de todos los commits a partir de una fecha/tiempo específico (una expresión de fecha, por ej., "1 week 2 days" o una fecha ISO):

`git diff 'HEAD@{3 months|weeks|days|hours|seconds ago}'`

- Muestra solo los nombres de los archivos cambiados con un commit específico:

`git diff --name-only {{commit}}`

- Muestra un resumen de la creación, renombre y modos de cambio con un commit específico:

`git diff --summary {{commit}}`

- Compara un único archivo entre dos ramas o commits:

`git diff {{rama_1}}..{{rama_2}} [--] {{ruta/al/archivo}}`

- Compara diferentes archivos de la rama actual con otra rama:

`git diff {{rama}}:{{ruta/al/archivo}} {{ruta/al/archivo2}}`
