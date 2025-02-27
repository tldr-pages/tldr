# git reflog

> Muestra un registro de cambios de las referencias (*reflog*) locales como HEAD, ramas o etiquetas.
> Más información: <https://git-scm.com/docs/git-reflog>.

- Muestra un registro de referencias para HEAD:

`git reflog`

- Muestra el registro de referencias para una rama:

`git reflog {{nombre_de_la_rama}}`

- Muestra solo las últimas 5 entradas en el registro de referencias:

`git reflog {{[-n|--max-count]}} 5`
