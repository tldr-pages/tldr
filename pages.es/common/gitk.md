# gitk

> Explora repositorios Git de forma gráfica.
> Vea también: `git-gui`, `git-cola`, `tig`.
> Más información: <https://git-scm.com/docs/gitk>.

- Muestra el explorador del repositorio Git actual:

`gitk`

- Muestra el explorador de repositorios para un archivo o directorio específico:

`gitk {{ruta/al/archivo_o_directorio}}`

- Muestra las confirmaciones realizadas desde hace una semana:

`gitk --since="hace 1 semana"`

- Muestra las confirmaciones anteriores al 1/1/2015:

`gitk --until="1/1/2015"`

- Muestra un máximo de 100 cambios en todas las ramas:

`gitk --max-count=100 --all`
