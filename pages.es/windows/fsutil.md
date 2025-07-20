# fsutil

> Mostrar información sobre volúmenes del sistema de archivos.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/fsutil>.

- Mostrar una lista de volúmenes:

`fsutil volume list`

- Mostrar información sobre el sistema de archivos de un volumen:

`fsutil fsInfo volumeInfo {{letra_de_unidad|ruta_del_volumen}}`

- Mostrar el estado actual de la reparación automática del sistema de archivos para todos los volúmenes:

`fsutil repair state`

- Mostrar el estado del bit sucio de todos los volúmenes:

`fsutil dirty query`

- Establecer el estado del bit sucio de un volumen:

`fsutil dirty set {{letra_de_unidad|ruta_del_volumen}}`
