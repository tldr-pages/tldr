# 7zr

> Un compresor de archivos con un alto ratio de compresión:
> Una versión independiente de `7z` que soporta únicamente arhivos .7z.
> Más información: <https://www.7-zip.org/>.

- Comprime un archivo o directorio:

`7zr a {{comprimido.7z}} {{ruta/al/archivo_o_directorio}}`

- Extrae un archivo 7z existente con la estructura original del directorio:

`7zr x {{comprimido.7z}}`

- Lista los contenidos de un archivo comprimido:

`7zr l {{comprimido.7z}}`
