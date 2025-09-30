# fsutil

> Muestra información sobre volúmenes del sistema de archivos.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/fsutil>.

- Muestra una lista de volúmenes:

`fsutil volume list`

- Muestra información sobre el sistema de archivos de un volumen:

`fsutil fsInfo volumeInfo {{letra_de_unidad|ruta_del_volumen}}`

- Muestra el estado actual de la reparación automática del sistema de archivos para todos los volúmenes:

`fsutil repair state`

- Muestra el estado del bit sucio de todos los volúmenes:

`fsutil dirty query`

- Establece el estado del bit sucio de un volumen:

`fsutil dirty set {{letra_de_unidad|ruta_del_volumen}}`
