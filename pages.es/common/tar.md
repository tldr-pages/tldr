# tar

> Herramienta para archivos.
> A veces combinada con un método de compresión, como gzip o bzip2.
> Más información: <https://www.gnu.org/software/tar>.

- Crea un archivo a partir de otros archivos:

`tar cf {{archivo_destino.tar}} {{archivo1}} {{archivo2}} {{archivo3}}`

- Crea un archivo comprimido con gzip:

`tar czf {{archivo_destino.tar.gz}} {{archivo1}} {{archivo2}} {{archivo3}}`

- Extrae un archivo (comprimido) en el directorio actual:

`tar xf {{archivo.tar[.gz|.bz2|.xz]}}`

- Extrae un archivo en un directorio:

`tar xf {{archivo.tar}} -C {{directorio}}`

- Crea un archivo comprimido usando el sufijo para determinar el programa de compresión:

`tar caf {{archivo_destino.tar.xz}} {{archivo1}} {{archivo2}} {{archivo3}}`

- Muestra el contenido de un archivo tar:

`tar tvf {{archivo.tar}}`

- Extrae archivos que coinciden con un patrón:

`tar xf {{archivo.tar}} --wildcards "{{*.html}}"`
