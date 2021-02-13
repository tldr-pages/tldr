# tar

> Herramienta para archivos.
> A veces combinada con un método de compresión, como gzip o bzip2.
> Más información: <https://www.gnu.org/software/tar>.

- Crear un archivo a partir de otros archivos:

`tar cf {{archivo_destino.tar}} {{archivo1}} {{archivo2}} {{archivo3}}`

- Crear un archivo comprimido con gzip:

`tar czf {{archivo_destino.tar.gz}} {{archivo1}} {{archivo2}} {{archivo3}}`

- Extraer un archivo (comprimido) en el directorio actual:

`tar xf {{archivo.tar[.gz|.bz2|.xz]}}`

- Extraer un archivo en un directorio:

`tar xf {{archivo.tar}} -C {{directorio}}`

- Crear un archivo comprimido usando el sufijo para determinar el programa de compresión:

`tar caf {{archivo_destino.tar.xz}} {{archivo1}} {{archivo2}} {{archivo3}}`

- Mostrar el contenido de un archivo tar:

`tar tvf {{archivo.tar}}`

- Extraer archivos que coinciden con un patrón:

`tar xf {{archivo.tar}} --wildcards "{{*.html}}"`
