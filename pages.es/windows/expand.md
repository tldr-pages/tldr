# expand

> Descomprimir archivos Cabinet de Windows.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/expand>.

- Descomprimir un archivo Cabinet de un solo archivo en el directorio especificado:

`expand {{ruta\al\archivo.cab}} {{ruta\al\directorio}}`

- Mostrar la lista de archivos en un archivo Cabinet de origen:

`expand {{ruta\al\archivo.cab}} {{ruta\al\directorio}} -d`

- Descomprimir todos los archivos del archivo Cabinet:

`expand {{ruta\al\archivo.cab}} {{ruta\al\directorio}} -f:*`

- Descomprimir un archivo específico de un archivo Cabinet:

`expand {{ruta\al\archivo.cab}} {{ruta\al\directorio}} -f:{{ruta\al\archivo}}`

- Ignorar la estructura de directorios al descomprimir y agregarlos a un solo directorio:

`expand {{ruta\al\archivo.cab}} {{ruta\al\directorio}} -i`
