# sdelete

> Elimina de forma segura archivos/directorios del disco, o limpia el espacio libre en un volumen/disco físico.
> Más información: <https://learn.microsoft.com/en-us/sysinternals/downloads/sdelete>.

- Eliminar archivos con 3 [p]asadas:

`sdelete -p 3 {{ruta\al\archivo1 ruta\al\archivo2 ...}}`

- Eliminar carpetas y sus [s]ubdirectorios con 1 pasada (por defecto):

`sdelete -s {{ruta\al\directorio1 ruta\al\directorio2 ...}}`

- Limpiar el espacio libre del volumen D: con 3 [p]asadas:

`sdelete -p 3 D:`

- Limpiar el espacio libre con ceros [z] del disco físico 2, que no debe contener volúmenes a limpiar:

`sdelete -z 2`
