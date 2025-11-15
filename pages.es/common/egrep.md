# egrep

> Encuentra patrones en archivos usando `regex` extendido ( admite `?`, `+`, `{}`, `()`, y `|`).
> Más información: <https://manned.org/egrep>.

- Busca un patrón dentro de un archivo:

`egrep "{{patrón_de_búsqueda}}" {{ruta/al/archivo}}`

- Busca un patrón en varios archivos:

`egrep "{{patrón_de_busqueda}}" {{ruta/al/archivo1 ruta/al/archivo2 ...}}`

- Busca un patrón en `stdin`:

`cat {{ruta/a/archivo}} | egrep {{patrón_de_búsqueda}}`

- Imprime el nombre del archivo y el número de línea de cada coincidencia:

`egrep {{[-H|--with-filename]}} {{[-n|--line-number]}} "{{patrón_de_búsqueda}}" {{ruta/al/archivo}}`

- Busca un patrón en todos los archivos de forma recursiva en un directorio, ignorando los archivos binarios:

`egrep {{[-r|--recursive]}} --binary-files={{without-match}} "{{patrón_de_búsqueda}}" {{ruta/al/directorio}}`

- Busca líneas que no coinciden con un patrón:

`egrep {{[-v|--invert-match]}} "{{patrón_de_búsqueda}}" {{ruta/al/archivo}}`
