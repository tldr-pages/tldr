# htmlq

> Utiliza selectores CSS para extraer contenido de archivos HTML.
> Más información: <https://github.com/mgdm/htmlq>.

- Devuelve todos los elementos de la clase `card`:

`cat {{ruta/al/archivo.html}} | htmlq '.card'`

- Obtiene el contenido del texto del primer párrafo:

`cat {{ruta/al/archivo.html}} | htmlq --text 'p:primer-del-tipo'`

- Encuentra todos los enlaces de una página:

`cat {{ruta/al/archivo.html}} | htmlq --attribute href 'a'`

- Elimina todas las imágenes y archivos SVG de una página:

`cat {{ruta/al/archivo.html}} | htmlq --remove-nodes 'img' --remove-nodes 'svg'`

- Impresión bonita y escritura de la salida en un archivo:

`htmlq --pretty --filename {{ruta/a/archivo.html}} --output {{ruta/a/salida.html}}`
