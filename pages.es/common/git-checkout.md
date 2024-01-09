# git checkout

> Comprueba una rama o rutas con el árbol de trabajo.
> Más información: <https://git-scm.com/docs/git-checkout>.

- Crea una nueva rama y se cambia a la misma:

`git checkout -b {{nombre_de_la_rama}}`

- Crea una nueva rama a partir de una referencia específica (rama, remoto/rama, las etiquetas son ejemplos de referencias válidas) y cambiarse a esta:

`git checkout -b {{nombre_de_la_rama}} {{referencia}}`

- Cambia a una rama local existente:

`git checkout {{nombre_de_la_rama}}`

- Cambia a la rama previamente comprobada:

`git checkout -`

- Cambia a una rama remota existente:

`git checkout --track {{nombre_remoto}}/{{nombre_de_la_rama}}`

- Descarta todos los cambios sin marcar en el directorio actual (véase `git reset` para más comandos para deshacer):

`git checkout .`

- Descarta los cambios no marcados de un archivo específico:

`git checkout {{nombre_del_archivo}}`

- Reemplaza un archivo en el directorio actual con la versión de este en la confirmación de una rama específica:

`git checkout {{nombre_de_la_rama}} -- {{nombre_del_archivo}}`
