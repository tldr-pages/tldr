# git diff

> Muestra los cambios de los archivos rastreados.
> Más información: <https://git-scm.com/docs/git-diff>.

- Muestra los cambios sin marcar ni confirmación:

`git diff`

- Muestra todos los cambios sin confirmación, pero incluye los marcados:

`git diff HEAD`

- Muestra solo los cambios marcados pero que no tienen confirmación:

`git diff --staged`

- Muestra los cambios de todas las confirmaciones a partir de una fecha y/o tiempo específico (p. ej., `1 week 2 days` o una fecha ISO):

`git diff 'HEAD@{3 months|weeks|days|hours|seconds ago}'`

- Muestra solo los nombres de los archivos cambiados en una confirmación específica:

`git diff --name-only {{confirmación}}`

- Muestra un resumen de los cambios hecho en una confirmación (p. ej. permisos de un archivo):

`git diff --summary {{confirmación}}`

- Compara un único archivo entre dos ramas o confirmaciones:

`git diff {{rama_1}}..{{rama_2}} [--] {{ruta/al/archivo}}`

- Compara diferentes archivos de la rama actual con otra rama:

`git diff {{rama}}:{{ruta/al/archivo}} {{ruta/al/archivo2}}`
