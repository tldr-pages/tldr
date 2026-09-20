# doskey

> Administra macros, comandos de Windows y líneas de comandos.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/doskey>.

- Lista macros disponibles:

`doskey /macros`

- Crea una nueva macro:

`doskey {{nombre}} = "{{comando}}"`

- Crea una nueva macro para un ejecutable específico:

`doskey /exename={{nombre_del_ejecutable}} {{nombre}} = "{{comando}}"`

- Elimina una macro:

`doskey {{nombre}} =`

- Muestra todos los comandos que están almacenados en memoria:

`doskey /history`

- Guarda macros en un archivo para portabilidad:

`doskey /macros > {{ruta\al\archivo_macinit}}`

- Carga macros desde un archivo:

`doskey /macrofile = {{ruta\al\archivo_macinit}}`
