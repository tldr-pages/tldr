# htmlq

> Utiliza selectores CSS para extraer contenido de archivos HTML.
> Más información: <https://github.com/mgdm/htmlq#usage>.

- Devuelve todos los elementos de la clase `card`:

`cat {{ruta/al/archivo.html}} | htmlq '.card'`

- Obtiene el contenido del texto del primer párrafo:

`cat {{ruta/al/archivo.html}} | htmlq {{[-t|--text]}} 'p:primer-del-tipo'`

- Encuentra todos los enlaces de una página:

`cat {{ruta/al/archivo.html}} | htmlq {{[-a|--attribute]}} href 'a'`

- Elimina todas las imágenes y archivos SVG de una página:

`cat {{ruta/al/archivo.html}} | htmlq {{[-r|--remove-nodes]}} 'img' {{[-r|--remove-nodes]}} 'svg'`

- Impresión bonita y escritura de la salida en un archivo:

`htmlq {{[-p|--pretty]}} {{[-f|--filename]}} {{ruta/al/archivo.html}} {{[-o|--output]}} {{ruta/a/salida.html}}`
