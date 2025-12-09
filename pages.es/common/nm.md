# nm

> Lista los nombres de símbolos en los archivos objeto.
> Más información: <https://manned.org/nm>.

- Lista de funciones globales (externas) en un archivo (con prefijo T):

`nm -g {{ruta/al/archivo.o}}`

- Lista solo los símbolos no definidos en un archivo:

`nm -u {{ruta/al/archivo.o}}`

- Lista todos los símbolos, incluso símbolos de depuración:

`nm -a {{ruta/al/archivo.o}}`

- Reconstruye símbolos C++ (hace que sean legibles):

`nm --demangle {{ruta/al/archivo.o}}`
