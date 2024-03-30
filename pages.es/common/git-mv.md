# git mv

> Mueve o renombra archivos y actualiza el índice Git.
> Más información: <https://git-scm.com/docs/git-mv>.

- Mueve el archivo dentro del repositorio y añade el movimiento al siguiente commit:

`git mv {{ruta/al/archivo}} {{nueva/ruta/al/archivo}}`

- Renombra un archivo y añade el renombre al siguiente commit:

`git mv {{nombre_de_archivo}} {{nuevo_nombre_de_archivo}}`

- Sobrescribe el archivo en la ruta objetivo si existe:

`git mv --force {{archivo}} {{objetivo}}`
