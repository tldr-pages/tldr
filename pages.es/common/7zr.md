# 7zr

> Archivador de ficheros con un alto ratio de compresión.
> Similar a `7z` excepto que sólo soporta ficheros 7z.
> Más información: <https://manned.org/7zr>.

- [a]rchiva un archivo o directorio:

`7zr a {{ruta/al/archivo.7z}} {{ruta/al/archivo_o_directorio}}`

- Cifra un archivo existente (incluidos los nombres de los archivos):

`7zr a {{ruta/al/archivo.7z}} -p{{contraseña}} -mhe={{on}} {{ruta/al/archivo.7z}}`

- E[x]trae un archivo conservando la estructura de directorios original:

`7zr x {{ruta/al/archivo.7z}}`

- E[x]trae un archivo a un directorio específico:

`7zr x {{ruta/al/archivo.7z}} -o{{ruta/de/salida}}`

- E[x]trae un archivo a `stdout`:

`7zr x {{ruta/al/archivo.7z}} -so`

- [l]ista el contenido de un archivo:

`7zr l {{ruta/al/archivo.7z}}`

- Establece el nivel de compresión (más alto significa más compresión, pero más lento):

`7zr a {{ruta/al/archivo.7z}} -mx={{0|1|3|5|7|9}} {{ruta/al/archivo_o_directorio}}`
