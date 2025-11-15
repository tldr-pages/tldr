# rmdir

> Elimina un directorio y su contenido.
> En PowerShell, este comando es un alias de `Remove-Item`. Esta documentación está basada en la versión de Símbolo del sistema (`cmd`) de `rmdir`.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/rmdir>.

- Vea la documentación del comando equivalente en PowerShell:

`tldr remove-item`

- Elimina un directorio vacío:

`rmdir {{ruta\al\directorio}}`

- Elimina un directorio y su contenido de forma recursiva:

`rmdir {{ruta\al\directorio}} /s`

- Elimina un directorio y su contenido de forma recursiva sin pedir confirmación:

`rmdir {{ruta\al\directorio}} /s /q`
