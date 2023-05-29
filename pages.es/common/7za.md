# 7za

> Archivador de archivos con una alta relación de compresión.
> Similar a `7z`, salvo que admite menos tipos de archivos pero es multiplataforma.
> Más información: <https://manned.org/7za>.

- [a]rchivar un archivo o directorio:

`7za a {{ruta/al/archivo.7z}} {{ruta/al/archivo_o_directorio}}`

- Encriptar un archivo existente (incluyendo nombres de archivos):

`7za a {{ruta/al/encriptado.7z}} -p{{contraseña}} -mhe={{on}} {{ruta/al/archivo.7z}}`

- E[x]traer un archivo preservando la estructura de directorios originales:

`7za x {{ruta/al/archivo.7z}}`

- E[x]traer un archivo a un directorio específico:

`7za x {{ruta/al/archivo.7z}} -o{{ruta/de/salida}}`

- E[x]traer un archivo a `stdout`:

`7za x {{ruta/al/archivo.7z}} -so`

- [a]rchivar usando un tipo de archivo específico:

`7za a -t{{7z|bzip2|gzip|lzip|tar|...}} {{ruta/al/archivo.7z}} {{ruta/al/archivo_o_directorio}}`

- [l]ista los contenidos de un archivo:

`7za l {{ruta/al/archivo.7z}}`

- Lista tipos de archivos disponibles:

`7za i`
