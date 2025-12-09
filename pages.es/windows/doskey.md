# doskey

> Administrar macros, comandos de Windows y líneas de comandos.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/doskey>.

- Listar macros disponibles:

`doskey /macros`

- Crear una nueva macro:

`doskey {{nombre}} = "{{comando}}"`

- Crear una nueva macro para un ejecutable específico:

`doskey /exename={{nombre_del_ejecutable}} {{nombre}} = "{{comando}}"`

- Eliminar una macro:

`doskey {{nombre}} =`

- Mostrar todos los comandos que están almacenados en memoria:

`doskey /history`

- Guardar macros en un archivo para portabilidad:

`doskey /macros > {{ruta\al\archivo_macinit}}`

- Cargar macros desde un archivo:

`doskey /macrofile = {{ruta\al\archivo_macinit}}`
