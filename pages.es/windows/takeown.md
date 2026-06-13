# takeown

> Toma posesión de un archivo o directorio.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/takeown>.

- Tomar posesión del archivo especificado:

`takeown /f {{ruta\al\archivo}}`

- Tomar posesión del directorio especificado:

`takeown /d {{ruta\al\directorio}}`

- Tomar posesión del directorio especificado y todos sus subdirectorios:

`takeown /r /d {{ruta\al\directorio}}`

- Cambiar la propiedad al grupo Administradores en lugar del usuario actual:

`takeown /a /f {{ruta\al\archivo}}`
