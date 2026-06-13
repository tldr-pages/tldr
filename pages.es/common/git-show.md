# git show

> Muestra varios tipos de objetos Git (confirmaciones, etiquetas, etcétera).
> Más información: <https://git-scm.com/docs/git-show>.

- Muestra información sobre la última confirmación (hash, mensaje, cambios y otros metadatos):

`git show`

- Muestra información de una confirmación específica:

`git show {{confirmación}}`

- Muestra información de la confirmación asociada a una determinada etiqueta:

`git show {{etiqueta}}`

- Muestra información de la tercera confirmación desde la punta de una rama:

`git show {{rama}}~{{3}}`

- Muestra el mensaje de una confirmación en una única línea, eliminando el resultado de la diferencia:

`git show --oneline -s {{confirmación}}`

- Muestra solo estadísticas (caracteres agregados o removidos) de los archivos modificados:

`git show --stat {{confirmación}}`

- Muestra solo la lista de archivos agregados, renombrados o eliminados:

`git show --summary {{confirmación}}`

- Muestra el contenido de un archivo en una revisión específica (por ej., una rama, una etiqueta o una confirmación):

`git show {{revisión}}:{{ruta/al/archivo}}`
