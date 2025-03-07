# atool

> Administra archivos comprimidos en varios formatos.
> Más información: <https://www.nongnu.org/atool/>.

- Muestra los archivos dentro de un archivo Zip:

`atool --list {{ruta/al/archivo.zip}}`

- Extrae un archivo tar.gz en un nuevo subdirectorio (o en el directorio actual si contiene solo un archivo):

`atool --extract {{ruta/al/archivo.tar.gz}}`

- Crea un nuevo archivo 7z con dos archivos:

`atool --add {{ruta/al/archivo.7z}} {{ruta/al/archivo1 ruta/al/archivo2 ...}}`

- Extrae todos los archivos Zip y rar en el directorio actual:

`atool --each --extract {{*.zip *.rar}}`
