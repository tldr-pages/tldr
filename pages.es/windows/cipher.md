# cipher

> Muestra o altera la encriptación de directorios y archivos en volúmenes NTFS.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/cipher>.

- Mostrar información sobre un archivo o directorio encriptado específico:

`cipher /c:{{ruta\al\archivo_o_directorio}}`

- [e]ncriptar un archivo o directorio (los archivos añadidos posteriormente al directorio también se encriptan a medida que el directorio se marca):

`cipher /e:{{ruta\al\archivo_o_directorio}}`

- [d]ecriptar un archivo o directorio:

`cipher /d:{{ruta\al\archivo_o_directorio}}`

- Eliminar de forma segura un archivo o directorio:

`cipher /w:{{ruta\al\archivo_o_directorio}}`
