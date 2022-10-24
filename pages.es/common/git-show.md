# git show

> Muestra varios tipos de objetos Git (commits, etiquetas, etcétera).
> Más información: <https://git-scm.com/docs/git-show>.

- Muestra información sobre el último commit (hash, mensaje, cambios y otros metadatos):

`git show`

- Muestra información de un commit específico:

`git show {{commit}}`

- Muestra información del commit asociado a una determinada etiqueta:

`git show {{etiqueta}}`

- Muestra información del tercer commit desde la punta de una rama:

`git show {{rama}}~{{3}}`

- Muestra el mensaje de un commit en una única línea, eliminando el resultado de la diferencia:

`git show --oneline -s {{commit}}`

- Muestra solo estadísticas (caracteres agregados o removidos) de los archivos modificados:

`git show --stat {{commit}}`

- Muestra solo la lista de archivos agregados, renombrados o eliminados:

`git show --summary {{commit}}`

- Muestra el contenido de un archivo en una revisión específica (por ej., una rama, una etiqueta o un commit):

`git show {{revisión}}:{{ruta/al/archivo}}`
