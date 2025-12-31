# readarray

> Lee líneas de `stdin` en un arreglo.
> Más información: <https://www.gnu.org/software/bash/manual/bash.html#index-readarray>.

- Ingresa líneas en un arreglo de forma interactiva:

`readarray {{nombre_arreglo}}`

- Lee líneas de un archivo y las inserta en un arreglo:

`readarray {{nombre_arreglo}} < {{ruta/al/archivo.txt}}`

- Elimina los delimitadores finales (newline por defecto):

`readarray -t {{nombre_arreglo}} < {{ruta/al/archivo.txt}}`

- Copia como máximo el número de líneas especificado:

`readarray -n {{N}} {{nombre_arreglo}} < {{ruta/al/archivo.txt}}`
