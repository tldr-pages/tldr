# git show

> Muestra varios tipos de objetos Git (commits, etiquetas, etcétera).
> Más información: <https://git-scm.com/docs/git-show>.

- Muestra información sobre el último commit (mensaje, cambios y otros metadatos):

`git show`

- Muestra información de un commit específico:

`git show {{commit}}`

- Muestra información del commit asociado a una determinada etiqueta:

`git show {{etiqueta}}`

- Muestra información del tercer commit desde la punta de la rama:

`git show {{rama}}~{{3}}`

- Muestra un hash de commit y un mensaje en una única línea, eliminando la el resultado de la diferencia:

`git show --oneline -s {{commit}}`

- Muestra el contenido de una archivo en una revisión específica (por ej., una rama, una etiqueta o un commit):

`git show {{revisión}}:{{ruta/del/archivo}}`
