# expand

> Descomprime archivos Cabinet de Windows.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/expand>.

- Descomprime un archivo Cabinet de un solo archivo en el directorio especificado:

`expand {{ruta\al\archivo.cab}} {{ruta\al\directorio}}`

- Muestra la lista de archivos en un archivo Cabinet de origen:

`expand {{ruta\al\archivo.cab}} {{ruta\al\directorio}} -d`

- Descomprime todos los archivos del archivo Cabinet:

`expand {{ruta\al\archivo.cab}} {{ruta\al\directorio}} -f:*`

- Descomprime un archivo específico de un archivo Cabinet:

`expand {{ruta\al\archivo.cab}} {{ruta\al\directorio}} -f:{{ruta\al\archivo}}`

- Ignora la estructura de directorios al descomprimir y los agregar a un solo directorio:

`expand {{ruta\al\archivo.cab}} {{ruta\al\directorio}} -i`
