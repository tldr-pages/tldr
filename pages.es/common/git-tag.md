# git tag

> Crea, muestra, borra o verifica etiquetas.
> Una etiqueta es una referencia estática a una confirmación específica.
> Más información: <https://git-scm.com/docs/git-tag>.

- Muestra todas las etiquetas:

`git tag`

- Crea una etiqueta con el nombre especificado a partir de la confirmación actual:

`git tag {{nombre_de_la_etiqueta}}`

- Crea una etiqueta con el nombre especificado a partir de la confirmación señalada:

`git tag {{nombre_de_la_etiqueta}} {{confirmación}}`

- Crea una etiqueta anotada con el mensaje especificado:

`git tag {{nombre_de_la_etiqueta}} -m {{mensaje_de_la_etiqueta}}`

- Elimina la etiqueta con el nombre especificado:

`git tag -d {{nombre_de_la_etiqueta}}`

- Obtén las etiquetas actualizadas de upstreams:

`git fetch --tags`

- Muestra todas las etiquetas cuyos ancestros incluyan una confirmación específica:

`git tag --contains {{confirmación}}`
