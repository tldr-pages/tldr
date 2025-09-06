# latexpand

> Simplifica los archivos fuente LaTeX eliminando comentarios y resolviendo `\include`s, `\input`s, etc.
> Más información: <https://www.ctan.org/pkg/latexpand>.

- Simplifica el archivo fuente dado y guarda el resultado en el archivo de salida especificado:

`latexpand --output {{ruta/a/salida.tex}} {{ruta/al/archivo.tex}}`

- No elimina los comentarios:

`latexpand --keep-comments --output {{ruta/a/salida.tex}} {{ruta/al/archivo.tex}}`

- No expande `\include`s, `\input`s etc.:

`latexpand --keep-includes --output {{ruta/a/salida.tex}} {{ruta/al/archivo.tex}}`

- Expande `\usepackage`s hasta encontrar los archivos STY correspondientes:

`latexpand --expand-usepackage --output {{ruta/a/salida.tex}} {{ruta/al/archivo.tex}}`

- Incorpora el archivo BBL especificado:

`latexpand --expand-bbl {{ruta/a/bibliografía.bbl}} --output {{ruta/a/salida.tex}} {{ruta/al/archivo.tex}}`
