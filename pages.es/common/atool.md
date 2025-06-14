# atool

> Un script para gestionar archivos comprimidos de varios tipos.
> `atool` utiliza programas de compresión externos, pero proporciona una interfaz de línea de comandos coherente para listar, extraer, crear y gestionar archivos comprimidos.
> Más información: <https://manned.org/atool>.

- Lista archivos en un archivo comprimido:

`atool {{[-l|--list]}} {{ruta/al/archivo.zip}}`

- Extrae un archivo (crea un subdirectorio de forma segura si es necesario):

`atool {{[-x|--extract]}} {{archivo.tar.gz}}`

- Extrae un archivo a un directorio específico:

`atool {{[-X|--extract-to]}} {{ruta/al/directorio_de_salida}} {{archivo.rar}}`

- Muestra el contenido de un archivo específico de un archivo en la salida estándar (como `cat`):

`atool {{[-c|--cat]}} {{archivo.tar}} {{ruta/al/archivo_en_archivo.txt}}`

- Crea un nuevo archivo a partir de archivos y/o directorios especificados:

`atool {{[-a|--add]}} {{archivo_nuevo.zip}} {{ruta/al/archivo1 ruta/al/archivo2 ...}}`

- Lista los archivos de un archivo y envía la salida a través de un paginador:

`atool {{[-l|--list]}} {{[-p|--pager]}} {{archivo_grande.tar.bz2}}`

- Extrae varios archivos a la vez (cada uno a su propio subdirectorio si es necesario):

`atool {{[-x|--extract]}} {{[-e|--each]}} {{archivo1.zip}} {{archivo2.tar.gz}} {{*.rar}}`

- Reempaqueta un archivo de un formato a otro (por ejemplo, de .tar.gz a .tar.7z):

`atool {{[-r|--repack]}} {{archivo_antiguo.tar.gz}} {{archivo_nuevo.tar.7z}}`
