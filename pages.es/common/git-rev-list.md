# git rev-list

> Muestra las revisiones (commits) en orden cronológico inverso.
> Más información: <https://git-scm.com/docs/git-rev-list>.

- Muestra todos los commits de la rama actual:

`git rev-list {{HEAD}}`

- Imprime el último commit que cambió (agregó/editó/eliminó) un archivo específico en la rama actual:

`git rev-list -n 1 HEAD -- {{ruta/al/archivo}}`

- Muestra los commits más recientes a partir de una fecha y una rama específica:

`git rev-list --since={{'2019-12-01 00:00:00'}} {{nombre_de_rama}}`

- Muestra todos los commits fusionados en un commit específico:

`git rev-list --merges {{commit}}`

- Imprime el número de commits desde una etiqueta específica:

`git rev-list {{nombre_de_la_etiqueta}}..HEAD --count`
