# git blame

> Muestra el hash de la confirmación y el último autor de cada línea de un archivo.
> Más información: <https://git-scm.com/docs/git-blame>.

- Muestra el archivo con el nombre del autor y el hash de la confirmación en cada línea:

`git blame {{archivo}}`

- Muestra el archivo con correo electrónico del autor y hash de la confirmación en cada línea:

`git blame -e {{archivo}}`

- Muestra quien y que modificó de un archivo, a partir de una confirmación específica:

`git blame {{confirmación}} {{ruta/al/archivo}}`

- Muestra quien y que modificó de un archivo, a partir de la confirmación anterior a otra:

`git blame {{confirmación}}~ {{ruta/al/archivo}}`
