# fclones

> Eficaz buscador y eliminador de archivos duplicados.
> Más información: <https://github.com/pkolaczk/fclones>.

- Busca ficheros duplicados en el directorio actual:

`fclones group .`

- Busca archivos duplicados en varios directorios y almacena los resultados en la caché:

`fclones group --cache {{ruta/a/directorio1 ruta/a/directorio2}}`

- Busca archivos duplicados solo en el directorio especificado, omitiendo los subdirectorios y guarda los resultados en un archivo:

`fclones group {{ruta/a/directorio}} --depth 1 > {{ruta/al/archivo.txt}}`

- Mueve los archivos duplicados en un archivo de texto a un directorio diferente:

`fclones move {{ruta/a/directorio_objetivo}} < {{ruta/al/archivo.txt}}`

- Simula un enlace simbólico a un archivo de texto sin realmente enlazarlo:

`fclones link --soft < {{ruta/al/archivo.txt}} --dry-run 2> /dev/null`

- Elimina los archivos duplicados más recientes en el directorio actual sin almacenarlos en un archivo:

`fclones group . | fclones remove --priority newest`

- Preprocesa los archivos JPEG en el directorio actual utilizando un comando externo para eliminar sus datos EXIF antes de buscar duplicados:

`fclones group . --name '*.jpg' -i --transform 'exiv2 -d a $IN' --in-place`
