# mklink

> Crea enlaces simbólicos.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/mklink>.

- Crea un enlace simbólico a un archivo:

`mklink {{ruta\al\archivo_enlace}} {{ruta\al\archivo_fuente}}`

- Crea un enlace simbólico a un directorio:

`mklink /d {{ruta\al\directorio_enlace}} {{ruta\al\directorio_fuente}}`

- Crea un enlace duro a un archivo:

`mklink /h {{ruta\al\archivo_enlace}} {{ruta\al\archivo_fuente}}`

- Crea un punto de unión de directorio:

`mklink /j {{ruta\al\directorio_enlace}} {{ruta\al\archivo_fuente}}`
