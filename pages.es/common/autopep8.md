# autopep8

> Formatea el código Python según la guía de estilo PEP 8.
> Más información: <https://github.com/hhatto/autopep8>.

- Formatea un archivo a `stdout`, con una longitud de línea máxima personalizada:

`autopep8 {{ruta/al/archivo.py}} --max-line-length {{length}}`

- Formatea un fichero, mostrando un diff de los cambios:

`autopep8 --diff {{ruta/al/archivo}}`

- Formatea un fichero en su lugar y guarda los cambios:

`autopep8 --in-place {{ruta/al/archivo.py}}`

- Formatea recursivamente todos los archivos de un directorio y guarda los cambios:

`autopep8 --in-place --recursive {{ruta/al/directorio}}`
