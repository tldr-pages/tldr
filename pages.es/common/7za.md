# 7za

> Un compresor de archivos con un alto ratio de compresión.
> Una versión independiente de `7z` con soporte para una menor cantidad de tipos de archivo.
> Más información: <https://www.7-zip.org/>.

- Comprime un archivo o directorio:

`7za a {{comprimido.7z}} {{ruta/al/archivo_o_directorio}}`

- Extrae un archivo 7z existente con la estructura original del directorio:

`7za x {{comprimido}}`

- Comprime utilizando un tipo específico de archivo:

`7za a -t{{zip|gzip|bzip2|tar}} {{comprimido}} {{ruta/al/archivo_o_directorio}}`

- Muestra los tipos de archivo disponibles:

`7za i`

- Muestra los contenidos de un archivo comprimido:

`7za l {{comprimedo}}`
