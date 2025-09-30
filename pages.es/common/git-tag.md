# git tag

> Crea, muestra, borra o verifica etiquetas.
> Una etiqueta (tag) es una referencia estática a una confirmación (commit).
> Más información: <https://git-scm.com/docs/git-tag>.

- Muestra todas las etiquetas:

`git tag`

- Crea una etiqueta con el nombre especificado a partir de la confirmación actual:

`git tag {{nombre_de_la_etiqueta}}`

- Crea una etiqueta con el nombre especificado a partir de la confirmación señalada:

`git tag {{nombre_de_la_etiqueta}} {{confirmación}}`

- Crea una etiqueta anotada con el mensaje especificado:

`git tag {{nombre_de_la_etiqueta}} {{[-m|--message]}} {{mensaje_de_la_etiqueta}}`

- Elimina la etiqueta con el nombre especificado:

`git tag {{[-d|--delete]}} {{nombre_de_la_etiqueta}}`

- Obtén las etiquetas actualizadas del remoto (remote):

`git fetch {{[-t|--tags]}}`

- Envía una etiqueta al remoto:

`git push origin tag {{nombre_de_la_etiqueta}}`

- Muestra todas las etiquetas cuyos ancestros incluyen una confirmación específica:

`git tag --contains {{confirmación}}`
