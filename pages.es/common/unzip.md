# unzip

> Extrae archivos/directorios de archivos Zip.
> Vea también: `zip`.
> Más información: <https://manned.org/unzip>.

- Extrae todos los archivos/directorios de archivos específicos en el directorio actual:

`unzip {{ruta/a/archivo1.zip ruta/a/archivo2.zip ...}}`

- Extrae los archivos/directorios de archivos a una ruta específica:

`unzip {{ruta/a/archivo1.zip ruta/a/archivo2.zip ...}} -d {{ruta/al/resultado}}`

- Extrae los archivos/directorios de archivos a `stdout` junto con los nombres de archivos extraídos:

`unzip -c {{ruta/a/archivo1.zip ruta/a/archivo2.zip ...}}`

- Extrae un archivo creado en Windows, que contiene archivos con caracteres no ASCII en su nombre (por ejemplo, caracteres chinos o japoneses):

`unzip -O {{gbk}} {{ruta/a/archivo1.zip ruta/a/archivo2.zip ...}}`

- Enumera los contenidos de un archivo específico sin extraerlos:

`unzip -l {{ruta/a/archivo.zip}}`

- Extrae un archivo específico de un archivo:

`unzip -j {{ruta/a/archivo.zip}} {{ruta/al/archivo1_en_archivo ruta/al/archivo2_en_archivo ...}}`
