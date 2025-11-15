# git diff

> Muestra los cambios en los archivos rastreados.
> Más información: <https://git-scm.com/docs/git-diff>.

- Muestra cambios no preparados:

`git diff`

- Muestra todos los cambios no confirmados (incluyendo los preparados):

`git diff HEAD`

- Muestra sólo los cambios preparados (añadidos, pero aún no confirmados):

`git diff --staged`

- Muestra los cambios de todos los confirmados desde una fecha/hora dada (una expresión de fecha, por ejemplo "1 week 2 days" o una fecha ISO):

`git diff 'HEAD@{{{3 months|weeks|days|hours|seconds ago}}}'`

- Muestra estadísticas de diff, como archivos cambiados, histograma y total de inserciones/eliminaciones de líneas:

`git diff --stat {{confirmación}}`

- Muestra un resumen de creaciones de archivos, renombramientos y cambios de modo desde una confirmación dada:

`git diff --summary {{confirmación}}`

- Compara un único archivo entre dos ramas o confirmaciones:

`git diff {{rama_1}}..{{rama_2}} {{ruta/al/archivo}}`

- Compara distintos archivos de la rama actual con otra rama:

`git diff {{rama}}:{{ruta/al/archivo2}} {{ruta/al/archivo}}`
