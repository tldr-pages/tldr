# git rev-list

> Muestra las revisiones (confirmaciones) en orden cronológico inverso.
> Más información: <https://git-scm.com/docs/git-rev-list>.

- Muestra todas las confirmaciones de la rama actual:

`git rev-list {{HEAD}}`

- Imprime la última confirmación que cambió (agregó/editó/eliminó) un archivo específico en la rama actual:

`git rev-list -n 1 HEAD -- {{ruta/al/archivo}}`

- Muestra las confirmaciones más recientes a partir de una fecha y una rama específica:

`git rev-list --since={{'2019-12-01 00:00:00'}} {{nombre_de_rama}}`

- Muestra todas las confirmaciones fusionadas en una confirmación específica:

`git rev-list --merges {{confirmación}}`

- Imprime el número de confirmaciones desde una etiqueta específica:

`git rev-list {{nombre_de_la_etiqueta}}..HEAD --count`
